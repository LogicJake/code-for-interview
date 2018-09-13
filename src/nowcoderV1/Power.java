package nowcoderV1;

public class Power {
	public static double Power(double base, int exponent) {
		double res = 1;
		if (exponent < 0) {
			exponent = -exponent;
			for (int i = 0; i < exponent; i++) {
				res = res * base;
			}
			return 1 / res;
		}
		for (int i = 0; i < exponent; i++) {
			res = res * base;
		}
		return res;
	}
	
	public static void main(String[] args) {
		System.out.println(Power(2, 0));
		
	}
	
}
