public class StringStuff {
    public static void main (String[] args) {
        System.out.println("wazzaapp");
        String firstName = "Luka";
        
        // THE VALUE OF THE METHOD/FUNCTION CALL IS WHAEVER THAT METHOD/FUNCTON CALL RETURNS

        String fullName = firstName.concat("Doncic");
        System.out.println(fullName);
        System.out.println(fullName.toUpperCase());
        String trimmedName = fullName.trim();

        String name = "Lebron";
        int championships = 4;
        System.out.println(String.format("The player named {name} has {championships} championships."));
        
        
        // System.out.println(trimmedName.charAt(2));
    }
}



// name = Lebron
// championships = 4;
// print(f"the player named {name} has {championships} championships.")
