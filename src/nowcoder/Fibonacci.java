package nowcoder;

public class Fibonacci {
	public int Fibonacci(int n) {
		if (n == 0 || n == 1) {
			return n;
		}
		else
			return Fibonacci(n-1)+Fibonacci(n-2);
    }
	public static void main(String[] args) {
		Fibonacci fibonacci = new Fibonacci();
		System.out.println(fibonacci.Fibonacci(4));

	}

}
