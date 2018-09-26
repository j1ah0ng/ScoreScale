import java.util.Scanner;

public class Test {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		double score;

		do {
			score = s.nextDouble();
			System.out.println(Math.ceil(2*score*2.78)/2);
		} while(true);
	}
}
