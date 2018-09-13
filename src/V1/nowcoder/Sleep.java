package V1.nowcoder;

import java.util.Scanner;

public class Sleep {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in); // Scanner类
		int n, k, sum = 0;
		n = in.nextInt();
		k = in.nextInt();
		int[] a = new int[n];
		int[] b = new int[n];
		for (int i = 0; i < n; i++) {
			a[i] = in.nextInt();
		}
		for (int i = 0; i < n; i++) {
			b[i] = in.nextInt();
		}

		for (int i = 0; i < n; i++) {
			if (b[i] == 1) {
				sum += a[i];
			}
		}

		int sumOfZero = 0;
		for (int i = 0; i < n; i++) {
			if (b[i] == 0) {
				int tmp = 0;
				int end = i + k > n ? n : i + k;
				for (int j = i; j < end; j++) {
					if (b[j] == 0) {
						tmp += a[j];
					}
				}
				sumOfZero = tmp > sumOfZero ? tmp : sumOfZero;
			}
		}
		System.out.println(sum+sumOfZero);
	}
}
