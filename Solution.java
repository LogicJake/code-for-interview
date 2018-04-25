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
import java.util.Stack;
import java.util.TreeMap;
import java.util.Map.*;


public class Solution {
	// Definition for a binary tree node.
	public class TreeNode {
	      int val;
	      TreeNode left;
	      TreeNode right;
	      TreeNode(int x) { val = x; }
	}
	
	class Employee {
	    // It's the unique id of each node;
	    // unique id of this employee
	    public int id;
	    // the importance value of this employee
	    public int importance;
	    // the id of direct subordinates
	    public List<Integer> subordinates;
	};
	
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
    
    public static boolean testIsPrime(int n){
        if (n <= 3) {
             return n > 1;
         }
         
        for(int i=2;i<=Math.sqrt(n);i++){
            if(n%i == 0)
                return false;
        }
        return true;
    }
    
    public int countPrimeSetBits(int L, int R) {
        int num = 0;
    	for(int i = L; i <= R; i++) {
        	String biString = Integer.toBinaryString(i);
        	int count = 0;
        	for (char c : biString.toCharArray()) {
				if (c == '1') 
					count++;
			}
        	if (testIsPrime(count)) {
				num++;
			}
        }
    	return num;
    }

    public boolean rotateString(String A, String B) {
        if(A.length() == 0 && B.length() == 0)
        	return true;
        else if(A.length() == 0 || B.length() == 0)
        	return false;
        char c = B.charAt(0);
        int index = 0;
    	while(index!=-1) {
        	if((A.substring(index, A.length())+A.substring(0,index)).equals(B))
        		return true;
        	else {
            	index = A.indexOf(c,index+1);
        	}
    	}
    	return false;
    }
    
    public double caluArea(double a,double b,double c) {
    	double s = (a+b+c)/2;
    	return Math.sqrt(s*(s-a)*(s-b)*(s-c));
    }
    
    public double largestTriangleArea(int[][] points) {
    	int N = points.length;
    	double res = 0;
    	for (int i = 0; i < N; ++i) {
            for (int j = i+1; j < N; ++j) {
                for (int k = j+1; k < N; ++k) {
                	double a = Math.sqrt(Math.pow(points[i][0]-points[j][0], 2)+Math.pow(points[i][1]-points[j][1], 2));
                	double b = Math.sqrt(Math.pow(points[i][0]-points[k][0], 2)+Math.pow(points[i][1]-points[k][1], 2));
                	double c = Math.sqrt(Math.pow(points[k][0]-points[j][0], 2)+Math.pow(points[k][1]-points[j][1], 2));
                	res = res<caluArea(a, b, c)?caluArea(a, b, c):res;
                }
            }
        }
    	return res;
    }

    public List<String> letterCasePermutation(String S) {
        List<String> res = new LinkedList<String>();
        res.add(S);
    	for (int i = 0; i < S.length(); i++) {
    		char c = S.charAt(i);
			if(c>'9') {
				int size = res.size();
				for (int j = 0; j < size; j++) {
					StringBuilder sBuilder = new StringBuilder(res.get(j));
					char c_1 = c>='a'?(char) (c-32):(char) (c+32);
					sBuilder.setCharAt(i, c_1);
					res.add(sBuilder.toString());
				}
			}
		}
    	return res;	
    }
    
    int[][] grid;
    boolean[][] seen;
    
    public int area(int r, int c) {
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length ||
                seen[r][c] || grid[r][c] == 0)
            return 0;
        seen[r][c] = true;
        return (1 + area(r+1, c) + area(r-1, c)
                  + area(r, c-1) + area(r, c+1));
    }
    
    public int maxAreaOfIsland(int[][] grid) {
        this.grid = grid;
        seen = new boolean[grid.length][grid[0].length];
        int ans = 0;
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[0].length; c++) {
                ans = Math.max(ans, area(r, c));
            }
        }
        return ans;
    }
    
    public int getImportance(List<Employee> employees, int id) {
		int res = 0; 
    	Map<Integer,Employee> mapEmployees = new HashMap<Integer,Employee>();
		for (int i = 0; i < employees.size(); i++)
			mapEmployees.put(employees.get(i).id, employees.get(i));
		Stack<Employee> stack = new Stack<Employee>();
		stack.push(mapEmployees.get(id));
		while(!stack.empty()) {
			Employee tmp = stack.pop();
			res += tmp.importance;
			for (int i = 0; i < tmp.subordinates.size(); i++)
				stack.push(mapEmployees.get(tmp.subordinates.get(i)));
		}
		return res;
    }

    public String mostCommonWord(String paragraph, String[] banned) {
    	
    	String res = null;
    	int num = 0;
    	
    	paragraph = paragraph.replace("!", "").replace(",", "").replace(".", "").replace("?","").replace("'", "").replace(";", "");
    	String[] ss = paragraph.split(" ");
    	Map<String,Integer> words = new HashMap<String,Integer>();
    	for (String string : ss) {
    		String s = string.toLowerCase();
    		List<String> bannedList = Arrays.asList(banned);
    		if(!bannedList.contains(s)) {
    			words.put(string.toLowerCase(), words.getOrDefault(string.toLowerCase(), 0)+1);
    			if(words.get(string.toLowerCase())>num) {
    				num = words.get(string.toLowerCase());
    				res = string.toLowerCase();
    			}
    		}
		}
    	return res;
    }

    public int rotatedDigits(int N) {
        int num = 0;
    	for (int i = 1; i <= N; i++) {
			String string = Integer.toString(i);
			if (string.contains("3")||string.contains("4")||string.contains("7"))
				continue;
			if (string.contains("2")||string.contains("5")||string.contains("6")||string.contains("9"))
				num++;
		}
    	return num;
    }
    
    public boolean find(TreeNode root, int k, Set < Integer > set) {
        if (root == null)
            return false;
        if (set.contains(k - root.val))
            return true;
        set.add(root.val);
        return find(root.left, k, set) || find(root.right, k, set);
    }
    
    
    public boolean findTarget(TreeNode root, int k) {
    	Set < Integer > set = new HashSet();
    	return find(root, k, set);
    }
    
    public String tree2str(TreeNode t) {
        String reString = "";
        if (t==null)
        	return reString;
        if (t.left == null && t.right == null)        
        	reString = Integer.toString(t.val);
        else if (t.right == null)
        	reString = Integer.toString(t.val)+"("+tree2str(t.left)+")";
        else
    	    reString = Integer.toString(t.val)+"("+tree2str(t.left)+")"+"("+tree2str(t.right)+")";
        return reString;
    }
    
    public boolean isOneBitCharacter(int[] bits) {
    	int i = 0;
    	if (bits.length == 1) {
			return true;
		}
        while(i < bits.length-1) {
			if(bits[i] == 0)
				i++;
			else
				i = i+2;
		}
        if (i == bits.length-1)
        	return true;
        return false;
    }
    
    public int countNode(TreeNode root) {
    	if(root == null)
    		return 0;
    	
    		return root.val+countNode(root.left);
    }
    private int sum = 0;
    public TreeNode convertBST(TreeNode root) {
        if (root != null) {
            convertBST(root.right);
            sum += root.val;
            root.val = sum;
            convertBST(root.left);
        }
        return root;
    }
    
    public int maxCount(int m, int n, int[][] ops) {
    	Map<Integer,Integer> M = new HashMap<>();
    	int maxNum = 0;
        for (int i = 0; i < ops.length; i++) {
        	int a = ops[i][0];
        	int b = ops[i][1];
			for (int j = 0; j <a; j++) {
				for (int j2 = 0; j2 < b; j2++) {
					M.put(j*n+j2, M.getOrDefault(j*n+j2, 0)+1);
					maxNum = Math.max(maxNum, M.get(j*n+j2));
				}
			}
		}
        int res = 0;
//        for (Entry<Integer, Integer> entry : M.entrySet()) {
//        	if(entry.getValue()==maxNum)
//        		res++;
//        }	
        if (maxNum == 0) {
        	return 0;
		}
        Iterator iter = M.keySet().iterator();
        while (iter.hasNext()) {
        	Object key = iter.next();
        	if (M.get(key) == maxNum) 
        		res++;
        }
        return res;
    }
    
    private boolean[][] visited;
    
    public void fill(int[][] image, int sr, int sc, int color, int newColor) {
    	System.out.println(sr+" "+sc+" "+image[sr][sc]);
    	if (image[sr][sc] == color) {
    		image[sr][sc] = newColor;
    		if (sr-1 >= 0 && !visited[sr-1][sc]) fill(image, sr-1, color, sc, newColor);
        	if (sr+1 < image.length && !visited[sr+1][sc]) fill(image, sr+1, sc, color, newColor);
        	if (sc+1 < image[0].length && !visited[sr][sc+1]) fill(image, sr, sc+1, color, newColor);
        	if (sc-1 >= 0 && !visited[sr][sc-1]) fill(image, sr, sc-1, color, newColor);
		}
    	visited[sr][sc] = true;
    }
    
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        this.visited = new boolean[image.length][image[0].length];
        if (image[sr][sc] != newColor)
        	fill(image,sr,sc,image[sr][sc],newColor);
        return image;
    }
    
    public int[][] floodFill2(int[][] image, int sr, int sc, int newColor) {
    	
    	if (image[sr][sc] != newColor)
        	fill(image,sr,sc,image[sr][sc],newColor);
        return image;
    }
    
    public int getMinimumDifference(TreeNode root) {
    	List<Integer> list = new LinkedList<Integer>();
    	traverse_binary_tree(root, list);
    	System.out.println(list.toString());
    	int res = Integer.MAX_VALUE;
    	for (int i = 0; i < list.size()-1; i++) {
			res = Math.min(res, Math.abs(list.get(i)-list.get(i+1)));
		}
    	return res;
    }
    
    public void traverse_binary_tree(TreeNode root,List<Integer> list) {
    	if (root == null) {
			return;
		}
    	traverse_binary_tree(root.left, list);
    	list.add(root.val);
        traverse_binary_tree(root.right, list);
    }
 
}
