public class StringManipulator {

    public void helloWorld() {
        System.out.println("Wazzaa lets manipulate some strings.");
    }

    public void helloWorld(String name) {
        System.out.println("Hello " + name + " Are you ready to manipulate some strings?.");
    }

    public String trimAndConcat(String str1, String str2) {
        System.out.println(str1.trim() + str2.trim());
        return "hello";
    }

    public Integer getIndexOrNull(String str1, char charmander) {
        if(str1.indexOf(charmander) == -1) {
            return null;
        }
        else {
            return str1.indexOf(charmander);
        }
    }

    public String concalSubstring(String str1, int int1, int int2, String str2) {
        string s1="javatpoint";
        System.out.println(s1.substring(int1,int2));

        return "wazzaa";
    }
    

    // public static void main(String[] args) {
    //     StringManipulator s1 = new StringManipulator();
    //     s1.helloworld();
    // }

}
