package nowcoder;

public class replaceSpace {
	/*
	 * 空间复杂度最小，在StringBuffer原来空间上拓展成替换后的空间大小
	 * 从左到右遍历算空格，从而计算替换后的长度，从右到左替换空格。
	 */
	public String replaceSpace(StringBuffer str) {
		int oldLen = str.length();
		int spaceNum = 0;
		for (int i = 0; i < str.length(); i++) {
			if (str.charAt(i) == ' ') {
				spaceNum++;
			}
		}
		// 拓展后的字符串长度等于原长度+2*空格长度
		str.setLength(oldLen + spaceNum * 2);
		int oldIndex = oldLen - 1;
		int newIndex = str.length() - 1;
		while (oldIndex >= 0 && newIndex >= 0) {
			if (str.charAt(oldIndex) != ' ') {
				str.setCharAt(newIndex--, str.charAt(oldIndex--));
			} else {
				str.setCharAt(newIndex--, '0');
				str.setCharAt(newIndex--, '2');
				str.setCharAt(newIndex--, '%');
				oldIndex--;
			}
		}
		return str.toString();
	}

	public static void main(String[] args) {
		replaceSpace replaceSpace = new replaceSpace();

		String string = "We Are  Happy";
		StringBuffer sBuffer = new StringBuffer(string);
		String res = replaceSpace.replaceSpace(sBuffer);
		System.out.println(res);
	}
}
