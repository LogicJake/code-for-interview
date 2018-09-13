package nowcoderV1;

public class ReOrderArray {
	public static void reOrderArray(int[] array) {
		int[] newArray = new int[array.length];
		int index = 0;
		for (int i : array) {
			if (i % 2 == 1) {
				newArray[index++] = i;
			}
		}
		for (int i : array) {
			if (i % 2 == 0) {
				newArray[index++] = i;
			}
		}
		for (int i = 0; i < newArray.length; i++) {
			array[i] = newArray[i];
		}
	}
	
	public static void main(String[] args) {
		int[] array = { 12, 2, 1, 8, 3 };
		reOrderArray(array);
		for (int i : array) {
			System.out.print(i + " ");
		}
	}
}
