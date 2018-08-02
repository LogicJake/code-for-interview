package nowcoder;

public class searchInTwoDimensionalArray {
	public boolean Find(int target, int[][] array) {
		if (array == null) {
			return false;
		}
		int rows = array.length;
		int cols = array[0].length;

		int row = 0;
		int col = cols - 1;

		while (row < rows && col >= 0) {
			if (array[row][col] == target) {
				return true;
			} else if (array[row][col] > target) {
				col--;
			} else {
				row++;
			}
		}
		
		return false;
	}

	public static void main(String[] args) {
		int[][] array = { { 1, 2, 8, 9 }, { 2, 4, 9, 12 }, { 4, 7, 10, 13 }, { 6, 8, 11, 15 } };
		searchInTwoDimensionalArray searchInTwoDimensionalArray = new searchInTwoDimensionalArray();

		boolean res = searchInTwoDimensionalArray.Find(1, array);
		System.out.println(res);
	}
}
