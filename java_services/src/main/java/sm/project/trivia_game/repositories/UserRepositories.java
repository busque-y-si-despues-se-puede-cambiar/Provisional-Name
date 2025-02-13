/*
 * This file has the definition of the user repositories in the application.
 * 
 * Author: Anderson David Arenas Gutierrez <adarenasg@uditrital.edu.co
 */

package sm.project.trivia_game.repositories;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Optional;

import org.json.JSONArray;
import org.json.JSONObject;
import org.springframework.stereotype.Repository;

import jakarta.annotation.PostConstruct;
import sm.project.trivia_game.data_objects.AuthDTO;
import sm.project.trivia_game.data_objects.UserDAO;

@Repository
public class UserRepositories {

    private final List<UserDAO> users = new ArrayList<>();
    // Absolute path to the file in shared_data.
    private final String path = "C:\\Users\\admin\\Documents\\Nueva_carpeta\\Provisional-Name\\shared_data\\Users.json";
    @PostConstruct
    public void init(){
        this.loadData();
    }

    private void loadData(){
        
        try (InputStream is = new FileInputStream(path)) {
            String content = new String(is.readAllBytes(), StandardCharsets.UTF_8);
            JSONObject jsonObjectTemp = new JSONObject(content);
            JSONArray jsonArray = jsonObjectTemp.getJSONArray("users");
            for (int i = 0; i < jsonArray.length(); i++){
                JSONObject jsonObject = jsonArray.getJSONObject(i);
                UserDAO user = new UserDAO(
                    jsonObject.getInt("id"),
                    jsonObject.getString("username"),
                    jsonObject.getString("password"),
                    jsonObject.getInt("score")
                );
                if (jsonObject.has("admin")) {
                    user.admin = jsonObject.getBoolean("admin");
                }
                users.add(user);
            }
        } catch (FileNotFoundException fnfEx) {
            System.err.println("File not found at path: " + path);
            fnfEx.printStackTrace();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    /*
    * This method saves the data in the file.
    */
    private void saveData() {
        try (FileWriter file = new FileWriter(path)) {
            JSONArray jsonArray = new JSONArray();
            for (UserDAO user : users) {
                JSONObject jsonObject = new JSONObject(new LinkedHashMap<>()); // Maintains insertion order
                jsonObject.put("id", user.id);
                jsonObject.put("username", user.username);
                jsonObject.put("password", user.password);
                jsonObject.put("score", user.score);
                jsonObject.put("online", user.online);
                jsonObject.put("admin", user.admin);
                jsonArray.put(jsonObject);
            }

            JSONObject root = new JSONObject(new LinkedHashMap<>()); // Maintains the order of the "users" key
            root.put("users", jsonArray);

            file.write(root.toString(4)); // Indentation for better readability
            file.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /*
     * This method returns the user by id.
     * 
     * @param id the user id.
     * 
     * @return the user by id.
     */
    public Optional<UserDAO> getById(Integer id) {
        for (UserDAO user : this.users) {
            if (user.id == id) {
                return Optional.of(user);
            }
        }
        return Optional.empty();
    }

    /*
    * This method validates a user authentication.
    * 
    * @param authData the user authentication data.
    * 
    * @return the user authenticated
    */
    public Optional<UserDAO> login(AuthDTO authData) {
        for (UserDAO user : this.users) {
            user.online = false;
        }

        for (UserDAO user : this.users) {
            if (user.username.equals(authData.getUsername()) && user.password.equals(authData.getPassword())) {
                user.online = true;
                saveData();
                return Optional.of(user);
            }
        }
        
        return Optional.empty();
    }

     /*
     * This method creates a new user.
     * 
     * @param user the user data.
     * 
     * @return the user created.
     */
    public Optional<UserDAO> create(AuthDTO authData) {
        int lastId = 0;
        for (int i = 0; i < users.size(); i++) {
            if (users.get(i).id > lastId) {
                lastId = users.get(i).id;
            }
        }
        lastId++;

        UserDAO newUser = new UserDAO(
            lastId, 
            authData.getUsername(), 
            authData.getPassword(),
            0
            );
        this.users.add(newUser);
        saveData();
        return Optional.of(newUser);
    }

    /*
     * This method logs out the currently online user.
     * 
     * @return the user that was logged out, or empty if no user was online.
     */
    public Optional<UserDAO> logout() {
        for (UserDAO user : this.users) {
            if (user.online) {
                user.online = false;
                saveData();
                return Optional.of(user);
            }
        }
        return Optional.empty();
    }
}
