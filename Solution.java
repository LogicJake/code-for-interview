package leetcoede;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;


public class Solution {
	// Definition for a binary tree node.
	public class TreeNode {
	      int val;
	      TreeNode left;
	      TreeNode right;
	      TreeNode(int x) { val = x; }
	}
	
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
	
	public int uniqueMorseRepresentations(String[] words) {
        String[] Morse = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
		Set<String> reSet = new HashSet<>();
        for (int i = 0; i < words.length; i++) {
			String tString = "";
			for (int j = 0; j < words[i].length(); j++) {
				tString += Morse[words[i].charAt(j)-'a'];
			}
			reSet.add(tString);
		}
        return reSet.size();
    }

	public double findMedianSortedArrays(int[] nums1, int[] nums2) {
		int m = nums1.length;
		int n = nums2.length;
		int[] nums = new int[m+n];
		int i = 0;
		int j = 0;
		int k = 0;
		while (i < m && j < n) {
			if(nums1[i] < nums2[j])
			{
				nums[k++] = nums1[i];
				i++;
			}
			else {
				nums[k++] = nums2[j];
				j++;
			}
		}
		while (i < m) {
			nums[k++] = nums1[i];
			i++;
		}
		while (j < n) {
			nums[k++] = nums2[j];
			j++;
		}
		int index1 = 0;
		int index2 = 0;
		
		if((m+n)%2==0) {
			index1 = (m+n)/2-1;
			index2 = (m+n)/2;
		}
		else {
			index1 = index2 = (m+n)/2;
		}
		return (nums[index1]+nums[index2])/2.0;
	}
	
	public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
		if (t1 == null)
            return t2;
        if (t2 == null)
            return t1;
        t1.val += t2.val;
        t1.left = mergeTrees(t1.left, t2.left);
        t1.right = mergeTrees(t1.right, t2.right);
        return t1;
	}
}
