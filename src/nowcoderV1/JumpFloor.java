package nowcoderV1;

public class JumpFloor {
	public int JumpFloor(int target) {
		if (target <= 2) {
			return target;
		}
		return JumpFloor(target-1)+JumpFloor(target-2);
	}

	public static void main(String[] args) {
		JumpFloor jumpFloor = new JumpFloor();
		System.out.println(jumpFloor.JumpFloor(4));
	}

}
