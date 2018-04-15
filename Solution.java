package leetcoede;

import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Set;
import java.util.TreeMap;


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

	public Boolean isDividing(int num) {
		int num_o = num;
		while(num > 0) {
			if(num%10 != 0 &&  num_o%(num%10)==0)
				num = num/10;
			else
				return false;
		}
		return true;
		
	}
	
	public List<Integer> selfDividingNumbers(int left, int right) {
		List<Integer> res = new LinkedList<Integer>();
		for(int i = left; i <= right; i++) {
			if(isDividing(i)) {
				res.add(i);
			}
		}
		return res;
    }
	
	public int arrayPairSum(int[] nums) {
        int res = 0;
		Arrays.sort(nums);
        for (int i = 0; i < nums.length; i+=2) {
			res+=nums[i];
		}
        return res;
    }

    public List<String> subdomainVisits(String[] cpdomains) {
    	Map<String,Integer> map = new HashMap<String, Integer>();
    	for (int i = 0; i < cpdomains.length; i++) {
			String[] splitstring = cpdomains[i].split(" ");
			int count = Integer.parseInt(splitstring[0]);
			String domain = splitstring[1];
			map.put(domain, map.getOrDefault(domain, 0)+count);
			while(domain.indexOf(".")!=-1) {
				domain = domain.substring(domain.indexOf(".")+1);
				map.put(domain, map.getOrDefault(domain, 0)+count);
			}
		}
    	List<String> res = new LinkedList<String>();
    	//或者用keySet遍历
    	Iterator<String> it = map.keySet().iterator();  
        while(it.hasNext()) {  
            String key = (String)it.next();  
            Integer value = map.get(key);
            String tmp = String.valueOf(value)+" "+key;
            res.add(tmp);
        }  
		return res;
    }
    
    public int[] numberOfLines(int[] widths, String S) {
    	int remindWidth = 100;
    	int lineNum = 1;
    	for (char c : S.toCharArray()) {
			int width = widths[c-'a'];
			if (width <= remindWidth) {
				remindWidth -= width;
			}
			else {
				lineNum++;
				remindWidth = 100-width;
			}
		}
    	int[] res = {lineNum,100-remindWidth};
    	return res;
    }
    
	private String reverseString(String string) {
		int i = 0;
		int j = string.length()-1;
		char[] lists = string.toCharArray();
		while(j>i) {
			char tmp = lists[i];
			lists[i] = lists[j];
			lists[j] = tmp;
			i++;
			j--;
		}
		return String.valueOf(lists);
	}
    
    public String reverseWords(String s) {
    	String[] ss = s.split(" ");
    	String reString = "";
    	for (int i = 0; i < ss.length; i++) {
    		if (i == 0) {
    			reString = reString+reverseString(ss[i]);
			}
    		else {
    			reString = reString+" "+reverseString(ss[i]);
			}
    		
		}
    	return reString;
    }

    public TreeNode trimBST(TreeNode root, int L, int R) {
        if (root == null) {
        	return root;
		}
        if (root.val < L)
			root = trimBST(root.right, L, R);
        else if (root.val > R) 
        {
        	root = trimBST(root.left, L, R);
		}
        else {
        	root.left = trimBST(root.left, L, R);
        	root.right = trimBST(root.right, L, R);
		}
        return root;
    }

    public int calPoints(String[] ops) {
        List<Integer> scores = new ArrayList<Integer>();		//stack结构更好
    	int res = 0;
        for (int i = 0; i < ops.length; i++) {
			switch (ops[i]) {
			case "+":{
				int this_score = scores.get(scores.size()-1)+scores.get(scores.size()-2);
				scores.add(this_score);
				break;
			}
			case "D":{
				int this_score = scores.get(scores.size()-1)*2;
				scores.add(this_score);
				break;
			}
			case "C":{
				scores.remove(scores.size()-1);
				break;
			}
			default:
				scores.add(Integer.parseInt(ops[i]));
				break;
			}
		}
        for (int i = 0; i < scores.size(); i++) {
			res += scores.get(i);
		}
        return res;
    }

    public int distributeCandies(int[] candies) {
    	//只需要知道种类数量，并不需要知道每个种类有多少个。所以用set而不是map
        Map<Integer, Integer> nums = new HashMap<Integer,Integer>();
    	for (int i = 0; i < candies.length; i++) {
			nums.put(candies[i], nums.getOrDefault(candies[i], 0)+1);
		}
    	System.out.println(nums);
    	if (nums.size() >= candies.length/2) {
			return candies.length/2;
		}
    	else {
    		return nums.size();
    	}
    }

    public boolean isToeplitzMatrix(int[][] matrix) {
    	//当且仅当r1 - c1 == r2 - c2，为对角线
    	int heigh = matrix.length;
    	int width = matrix[0].length;
    	for(int k = 0; k < width; k++) {
    		int i = 0;		//第一行查对角线
    		int j = k;
    		int number = matrix[i][j]; 		//起始值
    		i++;
    		j++;
    		while(i < heigh && j < width) {
    			if (matrix[i][j]!=number) {
					return false;
				}
    			i++;
    			j++;
    		}
    	}
    	for(int k = 0; k < heigh; k++) {
    		int i = k;		
    		int j = 0;	//第一列查对角线
    		int number = matrix[i][j]; 		//起始值
    		i++;
    		j++;
    		while(i < heigh && j < width) {
    			System.out.println(i+" "+j);
    			if (matrix[i][j]!=number) {
					return false;
				}
    			i++;
    			j++;
    		}
    	}
    	return true;
    }

    public int[][] matrixReshape(int[][] nums, int r, int c) {
    	int heigh = nums.length;
    	int width = nums[0].length;
    	if (r*c!=heigh*width) {
			return nums;
		}
    	else {
    		int k = 0;
    		int[][] res = new int[r][c];
    		for(int i = 0; i < r; i++)
    		{
    			for(int j = 0; j < c; j++)
    			{
    				res[i][j] = nums[k/width][k%width];
    				k++;
    			}
    		}
    		return res;
    	}
    }
    
    public List<Double> averageOfLevels(TreeNode root) {
    	List<Double> res = new LinkedList<Double>();
    	Queue<TreeNode> queue = new LinkedList<TreeNode>();
    	if (root == null) {
			return res;
		}
    	else
    	{
    		queue.add(root);
    		while (!queue.isEmpty()) {
				int num = queue.size();		//这一层有多少数据
				int i = num;
				double total = 0;
				while(i!=0) {
					TreeNode head = queue.poll();
					total += head.val;
					if (head.left!=null)
						queue.add(head.left);
					if(head.right!=null)
						queue.add(head.right);
					i--;
				}
				res.add(total/num);
			}
    		return res;
    	}
    }
    
    public int findLUSlength(String a, String b) {
        if (a.equals(b)) {
			return -1;
		}else {
			return Math.max(a.length(), b.length());
		}
    }
    
    public boolean hasAlternatingBits(int n) {
        int tmp = -1;
    	while(n!=0) {
    		if (tmp == n%2) {
				return false;
			}
    		tmp = n%2;
    		n /= 2;
        }
    	return true;
    }
}
