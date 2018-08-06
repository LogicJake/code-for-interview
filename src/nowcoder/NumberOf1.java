package nowcoder;

public class NumberOf1 {
	//自身不断右移，与1想与判断该位是否为1
		public int NumberOf1(int n) {
			int count = 0;
			while (n != 0) {
				if ((n & 1) != 0) {
					count++;
				}
				n = n >>> 1;	//无符号右移，因为负数补码右移最左边会补1导致死循环
			}
			return count;
		}
	
	//自身不动，移位flag，让他一步步左移。判断该位是否为1
	public int NumberOf1II(int n) {
		int count = 0;
		int flag = 1;
		while (flag != 0) {
			if ((n & flag) != 0) {
				count++;
			}
			flag = flag << 1;
		}
		return count;
	}
	
	public static void main(String[] args) {
		NumberOf1 numberOf1 = new NumberOf1();
		System.out.println(numberOf1.NumberOf1(5));
	}
	
}
