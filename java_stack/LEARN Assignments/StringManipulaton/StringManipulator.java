package java_stack.StringManipulaton;

public class StringManipulator {
    
    public String trimAndConcat(String a, String b){
        return a.trim().concat(b.trim());
    }
    public Integer getIndexOrNull(String str, char c) {
        if(str.indexOf(c) != -1) {
            return str.indexOf(c);
        }
        else {
            return null;
        }
    }


    public Integer getIndexOrNull(String a, String b) {
        if(a.indexOf(b) != -1) {
            return a.indexOf(b);
        }
        else {
            return null;
        }
    }


    public String concatSubstring(String a, int x, int y, String b) {
        return a.substring(x,y).concat(b);
    }
}
