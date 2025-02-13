/*
 * This file has the definition of the business logic for the user services.
 * 
 * Author: Anderson David Arenas Gutierrez <adarenasg@udistrital.edu.co>
 */

package sm.project.trivia_game.services;

import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import sm.project.trivia_game.data_objects.AuthDTO;
import sm.project.trivia_game.data_objects.UserDAO;
import sm.project.trivia_game.repositories.UserRepositories;

@Service
public class UserServices {

    @Autowired
    public UserRepositories userRepositories;
    
    /*
     * This method returns the user by id.
     * 
     * @param id the user id.
     * 
     * @return the user by id.
     */
    public Optional<UserDAO> getById(Integer id) {
        if (id == 0)
            return Optional.empty();
        return userRepositories.getById(id);
    }

    /*
     * This method validates an user authenticaion.
     * 
     * @param authData the user authentification data.
     * 
     * @return the user authenticated
     */
    public Optional<UserDAO> login(AuthDTO authData) {
        if (authData.getPassword() == null || authData.getUsername() == null)
            return Optional.empty();
        return userRepositories.login(authData);
    }

    /*
     * This method creates a new user.
     * 
     * @param user the user data.
     * 
     * @return the user created.
     */
    public Optional<UserDAO> create(AuthDTO authData) {
        if (authData.getUsername() == null || authData.getPassword() == null)
            return Optional.empty();
        return userRepositories.create(authData);
    }

    /*
    * This method logs out the currently online user.
    * 
    * @return the user that was logged out, or empty if no user was online.
    */
    public Optional<UserDAO> logout() {
        return userRepositories.logout();
    }

    /*
     * This method creates a new admin user.
     * 
     * Only an online admin user can create another admin.
     * 
     * @param authData the authentication data for the new admin user.
     * 
     * @return the created admin user.
     */
    public Optional<UserDAO> createAdmin(AuthDTO authData) {
        if (authData.getUsername() == null || authData.getPassword() == null)
            return Optional.empty();
        return userRepositories.createAdmin(authData);
    }
}
