import java.util.Scanner;
public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.print("Principal:");
        double principal = scanner.nextDouble();
        System.out.print("Annual Interest Rate:");
        double annual = scanner.nextDouble();
        System.out.print("Period(Years):");
        double period = scanner.nextInt();

        double n = period * 12;
        double r = annual / 12;

        double numerator = (Math.pow(1+r,n)*r);    // numerator = r * ((1+r)^n)
        double denominator = (Math.pow(1+r,n)-1);  // denominator = ((1+r)^n) - 1

        double m = principal * (numerator/denominator);
        System.out.print("Your monthly payment is: " + m);
    }
}
