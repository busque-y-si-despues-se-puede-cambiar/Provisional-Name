/*
 * This file has the definition of the user endpoints in the application.
 * 
 * Author: Anderson David Arenas Gutierrez <adarenasg@udistrital.edu.co>
 */

package sm.project.trivia_game.controllers;

import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import sm.project.trivia_game.data_objects.AuthDTO;
import sm.project.trivia_game.data_objects.UserDAO;
import sm.project.trivia_game.services.UserServices;

@RestController
@RequestMapping("/v1/user")
public class UserController {
    
    @Autowired
    private UserServices userServices;

    /*
     * This method returns the user by id.
     * 
     * @param id the user id.
     * 
     * @return the user by id.
     */
    @GetMapping("/getById/{idUser}")
    public Optional<UserDAO> getById(@PathVariable("idUser")Integer id) {
        return userServices.getById(id);
    }

    /*
     * This method validates an user authenticaion.
     * 
     * @param authData the user authentification data.
     * 
     * @return the user authenticated
     */
    @PostMapping("/login")
    public Optional<UserDAO> login(@RequestBody AuthDTO authData) {
        return userServices.login(authData);
    }

    /*
     * This method creates a new user.
     * 
     * @param user the user data.
     * 
     * @return the user created.
     */
    @PostMapping("/create")
    public Optional<UserDAO> create(@RequestBody AuthDTO authData) {
        return userServices.create(authData);
    }

    /*
    * This method logs out the currently online user.
    * 
    * @return the user that was logged out, or empty if no user was online.
    */
    @PostMapping("/logout")
    public Optional<UserDAO> logout() {
        return userServices.logout();
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
    @PostMapping("/createAdmin")
    public Optional<UserDAO> createAdmin(@RequestBody AuthDTO authData) {
        return userServices.createAdmin(authData);
    }
}
