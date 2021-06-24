
// 


public class Chipotle {

    // create a function that will take a number. If the number is divisible by only 5, then it will say "queso and cheese". If the number is divisible by only 7, it will say "chipotle with extra meat and guac". If the number is divisible by both 5 and 7, then it will say "you get an XL burrito and queso and chips". For everything else it will say, "california tortilla doe".

    public static void welcomeToChipotle(int num) {
        if(num%5 == 0 && num%7 == 0) {
            Ststem.out.println("YOu get an XL burrito, queso, and chips.");
        } else {
            System.out.println("Everything else.");

        }
    }

    public static void main (String[] args) {
        System.out.println("testinggggg");
        Chipotle.welcomeToChipotle(35);
    }
}