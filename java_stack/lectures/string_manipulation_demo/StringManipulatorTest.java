public class StringManipulatorTest {
    public static void main(String[] args) {
        StringManipulator s1 = new StringManipulator();
        s1.helloWorld();
        s1.helloWorld("Lebron");
        s1.trimAndConcat("       robinhood", "             please stop");

        System.out.println(s1.getIndexOrNull("Trucks", '4'));
        System.out.println(s1.getIndexOrNull("Luka Magic", 'M'));
        System.out.println(s1.getIndexOrNull("Pantera", 'a'));
        System.out.println(s1.getIndexOrNull("The Lake", 'k'));
        System.out.println(s1.getIndexOrNull("Motorcycles", 'y'));
        // s1.getIndexOrNull("Calamari", 'x');
        s1.concatSubstring("Garfield", 3, 6, "wazzaa");
        s1.concatSubstring("YoungMoney", 6, 6, "wazzaa");


    }
}
