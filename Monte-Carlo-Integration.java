import java.util.Random;
import java.util.Scanner;

// Calculates the volume  of a sphere in n-dimensional space given the radius.
// A sphere in 4-dimensional space or more is used by statistical mechanics, quantum mechanics, etc.

public class Main {
    public static void main(String[] args) {

        Scanner scn = new Scanner(System.in);
        System.out.println("Radius: ");
        double radius = scn.nextDouble();
        Scanner scn1 = new Scanner(System.in);
        System.out.println("Dimension: ");
        int dim = scn1.nextInt();
        int count = 0;
        double sum = 0;

        for (int x = 0; x < 100000; x++){
            Random r = new Random();
            for (int i = 0; i < dim; i++) {
                double randomValue = -(radius) + (radius - (-(radius))) * r.nextDouble();
                // System.out.println(randomValue);
                sum += randomValue * randomValue;
            }
            if (sum  - (radius * radius) <  0) {
                count += 1;
            }
            sum = 0;
        }
        System.out.println(((double)count / 100000) * (Math.pow((radius + radius ), dim)));
    }
}
