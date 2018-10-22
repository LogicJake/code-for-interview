package V2.nowcoder;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Vector;

/**
* Created by LogicJake on 2018年9月13日
* title：树的高度 
*  现在有一棵合法的二叉树，树的节点都是用数字表示，现在给定这棵树上所有的父子关系，求这棵树的高度
*/
public class TreeHeight {
	private static Map<Integer, Vector<Integer>> rootMap = new HashMap<Integer, Vector<Integer>>();
	
	public static int getHeight(int root) {
		Vector<Integer> children = rootMap.getOrDefault(root, new Vector<Integer>());
		if (children.size() == 0) {
			return 1;
		}
		int leftHeight = children.size() == 0 ? 0 : getHeight(children.get(0));
		int rightHeight = children.size() == 1 ? 0 : getHeight(children.get(1));
		return leftHeight > rightHeight ? leftHeight + 1 : rightHeight + 1;
	}
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		for (int i = 0; i < n - 1; i++) {
			int root = in.nextInt();
			int child = in.nextInt();
			Vector<Integer> children = rootMap.getOrDefault(root, new Vector<Integer>());
			children.add(child);
			rootMap.put(root, children);
		}
		System.out.println(getHeight(0));
		in.close();
	}
}
