public class WazzaaWorld {
    public static void main(String[] args) {
        System.out.println("Wazzzzzaaaa");
        System.out.println("Welcome to Java");


        // primitive variables

        int x = 15;
        Integer x2 = 15; // Integer is an object. int is a number. 

        System.out.println(x);

        double y;
        y = 3.14;
        System.out.println(y);

        String name = "Judge";
        Character charmander = '!'; // single quotes for char.

        // casting

        System.out.println(charmander.getClass());

        Integer y2Int = (int)y;
        System.out.println(y2Int);

        // null values

        // int test = 23; //cannot convert null to int. Have to use Integer.
        Integer test = null;

        

    }
}