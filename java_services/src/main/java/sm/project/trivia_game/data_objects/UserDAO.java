/*
 * This file has a data object class that represents the user data access object.
 * 
 * Author: Anderson David Arenas Gutierrez <adarenasg@udistrital.edu.co>
 */

package sm.project.trivia_game.data_objects;

/*
 * This class represents the user data access object.
 */
public class UserDAO {
        
    public int id;
    public String username;
    public String password;
    public int score;
    public boolean online;

    public UserDAO(int id, String username, String password, int score) {
        this.id = id;
        this.username = username;
        this.password = password;
        this.score = score;
        this.online = false;
    }
}
