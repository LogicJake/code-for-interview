package nowcoderV2;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;

/**
* Created by LogicJake on 2018年9月13日
* title：数串 
*  设有n个正整数，将他们连接成一排，组成一个最大的多位整数。
*  如:n=3时，3个整数13,312,343,连成的最大整数为34331213。
*  如:n=4时,4个整数7,13,4,246连接成的最大整数为7424613。
*/
public class MaxString {
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		while (in.hasNext()) {
			int n = in.nextInt();
			ArrayList<Integer> numbers = new ArrayList<>();
			for (int i = 0; i < n; i++) {
				numbers.add(in.nextInt());
			}
			Collections.sort(numbers, new Comparator<Integer>() {
				@Override
				public int compare(Integer o1, Integer o2) {
					String s1 = String.valueOf(o1);
					String s2 = String.valueOf(o2);
					return (s2 + s1).compareTo(s1 + s2);
				}
			});
			
			for (int i = 0; i < numbers.size(); i++) {
				System.out.print(numbers.get(i));
			}
		}
		in.close();
	}
}
