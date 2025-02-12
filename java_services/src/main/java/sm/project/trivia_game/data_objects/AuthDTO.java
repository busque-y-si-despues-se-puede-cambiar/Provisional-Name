/*
 * This file has a data object class that represents the authentification 
 * data transfer object.
 * 
 * Author: Anderson David Arenas Gutierrez <adarenasg@udistrital.edu.co>
 */

package sm.project.trivia_game.data_objects;

/*
 * This class represents the authentification data transfer object.
 */
public class AuthDTO {
    private String username = null;
    private String password = null;

    public AuthDTO(String username, String password) {
        this.username = username;
        this.password = password;
    }

    /*
     * This method returns the username.
     * 
     * @return the username.
     */
    public String getUsername() {
        return this.username;
    }

    /*
     * This method returns the password.
     * 
     * @return the password.
     */
    public String getPassword() {
        return this.password;
    }
}
