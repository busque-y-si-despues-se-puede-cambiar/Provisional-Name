/*
 * This file has the definition of the data object class for the admin user.
 * 
 * Author: Anderson David Arenas Gutierrez <adarenasg@udistrital.edu.co>
 */
package sm.project.trivia_game.data_objects;

/**
 * The AdminUserDAO class extends the UserDAO class and represents an admin user in the system.
 * It includes additional functionality specific to admin users.
 * 
 * <p>This class inherits the following properties from UserDAO:
 * <ul>
 *   <li>id - The unique identifier for the user.</li>
 *   <li>username - The username of the user.</li>
 *   <li>password - The password of the user.</li>
 *   <li>score - The score of the user.</li>
 * </ul>
 * 
 * <p>Additionally, this class sets the admin property to true and provides a method to manage the system.
 * 
 * @param id The unique identifier for the admin user.
 * @param username The username of the admin user.
 * @param password The password of the admin user.
 * @param score The score of the admin user.
 */
public class AdminUserDAO extends UserDAO {

    public AdminUserDAO(int id, String username, String password, int score) {
        super(id, username, password, score);
        this.admin = true;
    }

    public void manageSystem() {
        System.out.println("Administrando el sistema...");
    }
}