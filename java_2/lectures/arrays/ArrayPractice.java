import java.util.Arrays;
import java.util.ArrayList;

public class ArrayPractice {
    public static void main(String [] args) {
        // int[] x = new int[4];
        // x[0] = 5;
        // x[1] = 8;
        // x[2] = 3;
        // x[3] = 2;

        int[] x = {5, 8, 3, 2};
        System.out.println(Arrays.toString(x));
        x[0] = 23;
        System.out.println(Arrays.toString(x));


        // using ArrayList

        ArrayList<Integer> y = new ArrayList<Integer>();
        y.add(23);
        y.add(20);
        y.add(77);
        y.remove(y.size()-1);
        System.out.println(y);

        // creaing an array list with the values all at once.

        ArrayList<Integer> anothaOne = new ArrayList<Integer>(Arrays.asList(23,5,7,81,45));
        System.out.println(anothaOne);

        // multiple data types

        ArrayList<Object> mixedBag = new ArrayList<Object>(Arrays.asList(23,"Jordan",true,'a', 32.9));
        System.out.println(mixedBag);
    }
}