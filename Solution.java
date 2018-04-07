package leetcoede;

public class Solution {
	public int numJewelsInStones(String J, String S) {
		int num = 0;
		for(int i = 0; i < J.length(); i++) {
			for(int j = 0; j < S.length(); j++) {
				if(J.charAt(i) == S.charAt(j))
					num++;
			}
		}
        return num;
    }
}
