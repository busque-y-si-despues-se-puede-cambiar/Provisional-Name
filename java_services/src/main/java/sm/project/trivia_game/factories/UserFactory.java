/**
 * This file has the definition of the factory class for creating instances of UserDAO.
 * 
 * Author: Anderson David Arenas Gutierrez <adarenasg@udistrital.edu.co>
 */
package sm.project.trivia_game.factories;

import sm.project.trivia_game.data_objects.AdminUserDAO;
import sm.project.trivia_game.data_objects.UserDAO;

/**
 * Factory class for creating UserDAO objects.
 */
public class UserFactory {

    public static UserDAO createUser(int id, String username, String password, int score, boolean isAdmin) {
        if (isAdmin) {
            return new AdminUserDAO(id, username, password, score);
        }
        return new UserDAO(id, username, password, score);
    }
}

