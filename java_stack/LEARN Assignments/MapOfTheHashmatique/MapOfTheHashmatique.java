public class MapOfTheHashMatique {
    
}import java.util.HashMap;
import java.util.Set;

public class MapOfTheHashmatique{
    public void retriveSongData(){  
        HashMap<String, String> songMap = new HashMap<String, String>();
        songMap.put("Cosmic Rain", "...screams my name. I am cosmic rain.");
        songMap.put("Crown of Lies", "Heavy hangs your crown of lies.");
        songMap.put("Dont Come Home", "Been livin on the right side of wrong, gone done and pissed off the devil this time.");
        songMap.put("Right Back Up", "Goin down down down down down baby, till i hit the ground.");

        String single = songMap.get("Heavy hangs your crown of lies.");
        System.out.println(single);

        Set<String> keys = songMap.keySet();
        for(String key : keys){
            System.out.println(key);
            System.out.println(songMap.get(key));
        }
    }
}
