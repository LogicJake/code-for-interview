package V1.nowcoder;

public class NumberOf1 {
	//���������ƣ���1�����жϸ�λ�Ƿ�Ϊ1
		public int NumberOf1(int n) {
			int count = 0;
			while (n != 0) {
				if ((n & 1) != 0) {
					count++;
				}
				n = n >>> 1;	//�޷������ƣ���Ϊ����������������߻Ჹ1������ѭ��
			}
			return count;
		}
	
	//����������λflag������һ�������ơ��жϸ�λ�Ƿ�Ϊ1
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
