package V1.nowcoder;

public class ReplaceSpace {
	/*
	 * �ռ临�Ӷ���С����StringBufferԭ���ռ�����չ���滻��Ŀռ��С
	 * �����ұ�����ո񣬴Ӷ������滻��ĳ��ȣ����ҵ����滻�ո�
	 */
	public String replaceSpace(StringBuffer str) {
		int oldLen = str.length();
		int spaceNum = 0;
		for (int i = 0; i < str.length(); i++) {
			if (str.charAt(i) == ' ') {
				spaceNum++;
			}
		}
		// ��չ����ַ������ȵ���ԭ����+2*�ո񳤶�
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
		ReplaceSpace replaceSpace = new ReplaceSpace();

		String string = "We Are  Happy";
		StringBuffer sBuffer = new StringBuffer(string);
		String res = replaceSpace.replaceSpace(sBuffer);
		System.out.println(res);
	}
}
