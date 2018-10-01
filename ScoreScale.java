import java.util.Scanner;

public class ScoreScale {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		double scale;
		double score;

		System.print("Enter the scale factor: ");
		scale = s.nextDouble();
		System.println();

		do {
			System.out.print("Score: ");
			score = s.nextDouble();
			System.out.println();
			System.out.println(Math.ceil(2*score*2.78)/2);
		} while(true);
	}
}
