package nowcoderV1;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

public class Fruit {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in); // Scanner类
		int n, k;
		n = in.nextInt();
		int[] a = new int[n];

		for (int i = 0; i < n; i++) {
			a[i] = in.nextInt();
		}
		k = in.nextInt();
		int[] b = new int[k];

		for (int i = 0; i < k; i++) {
			b[i] = in.nextInt();
		}

		Map<Integer, Integer> res = new HashMap<>();
		Set<Integer> hasFind = new HashSet<>();
		int[] sum = new int[n + 1];
		sum[0] = 0;
		for (int i = 1; i < n + 1; i++) {
			sum[i] = sum[i - 1] + a[i - 1];
			for (int j = 0; j < k; j++) {
				if (!hasFind.contains(b[j]) && sum[i] >= b[j]) {
					res.put(b[j], i);
					hasFind.add(b[j]);
				}
			}
		}
		
		for (int i = 0; i < k; i++) {
			System.out.println(res.get(b[i]));
		}

	}
}
