/*
 * This file has the definition of the user repositories in the application.
 * 
 * Author: Anderson David Arenas Gutierrez <adarenasg@uditrital.edu.co
 */

package sm.project.trivia_game.repositories;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
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

    @PostConstruct
    public void init(){
        this.loadData();
    }

    private void loadData(){
        // Absolute path to the file in shared_data.
        String path = "C:\\Users\\admin\\Documents\\Nueva_carpeta\\Provisional-Name\\shared_data\\Users.json";
        try (InputStream is = new FileInputStream(path)) {
            String content = new String(is.readAllBytes(), StandardCharsets.UTF_8);
            JSONArray jsonArray = new JSONArray(content);
            for (int i = 0; i < jsonArray.length(); i++){
                JSONObject jsonObject = jsonArray.getJSONObject(i);
                UserDAO user = new UserDAO(
                    jsonObject.getInt("id"),
                    jsonObject.getString("username"),
                    jsonObject.getString("password"),
                    jsonObject.getInt("score")
                );
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
            if (user.username.equals(authData.getUsername()) && user.password.equals(authData.getPassword())) {
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
    public Optional<UserDAO> create(UserDAO user) {
        int lastId = -1;
        for (UserDAO userTemp : this.users) {
            if (userTemp.id > lastId) {
                lastId = userTemp.id;
            }
        }
        lastId++;

        UserDAO newUser = new UserDAO(
            lastId, 
            user.username, 
            user.password,
            user.score
            );
        this.users.add(newUser);
        return Optional.of(newUser);
    }

    /*
     * This method updates the score of a user.
     * 
     * @param id the user id.
     * @param score the new score.
     * 
     * @return the updated user.
     */
    public Optional<UserDAO> updateScore(Integer id, Integer score) {
        for (UserDAO user : this.users) {
            if (user.id == id) {
                user.score = score;
                return Optional.of(user);
            }
        }
        return Optional.empty();
    }
}
