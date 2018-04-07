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
	
	public boolean judgeCircle(String moves) {
        int x = 0;
        int y = 0;
        for (int i = 0; i < moves.length(); i++) {
        	switch (moves.charAt(i)) {
			case 'U':
				y++;
				break;
			case 'D':
				y--;
				break;
			case 'R':
				x++;
				break;
			case 'L':
				x--;
				break;
			}
		}
        if (x ==0 && y == 0) {
			return true;
		}
		else {
	        return false;
		}
    }
}
