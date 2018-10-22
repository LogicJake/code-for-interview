package V1.nowcoder;

public class RectCover {
	public int RectCover(int target) {
		if (target <= 2) {
			return target;
		}
		return RectCover(target - 1) + RectCover(target - 2);
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
