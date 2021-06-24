public class LoopPractice {
    public static void printNagative23To77() {
        for(int i = -23; i<=77; i++ ) {
            System.out.println(i);
        }
    }

    public static void printEvenNumsFrom0ToNum(int num) {
        for(int i = 0; i<=num; i+=2) {
            System.out.println(i);
        }
    }

    public static int sumItUp(int num) {
        int sum = 0;
        for(int i = 0; i<=num; i++) {
            sum += i;
        }
        System.out.println(sum);
        return sum;
    }


    public static void main(String[] args) {
        System.out.println("wazzaa loop practice");
        // LoopPractice.printNagative23To77();

        // LoopPractice.printEvenNumsFrom0ToNum(500);

        LoopPractice.sumItUp(350);


    }
}
