package leetcoede.tree;

import java.util.LinkedList;
import java.util.List;
import java.util.Stack;

public class binaryTreeInorderTraversal {
	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;

		TreeNode(int x) {
			val = x;
		}
	}

	class Solution {
		private void Traversal(List<Integer> list,TreeNode root) {
			if (root == null) {
				return;
			}
			Traversal(list,root.left);
			list.add(root.val);
			Traversal(list,root.right);
		}
		
		private void Traversal2(List<Integer> list,TreeNode root) {		//µü´ú
			Stack<TreeNode> stack = new Stack<>();
			TreeNode pNode = root;
			while(pNode != null || !stack.isEmpty()) {
				while(pNode != null) {
					stack.push(pNode);
					pNode = pNode.left;
				}
				if (!stack.empty()) {
					pNode = stack.pop();
					list.add(pNode.val);
					pNode = pNode.right;
				}
			}
		}
		
		public List<Integer> inorderTraversal(TreeNode root) {
			List<Integer> res = new LinkedList<>();
			if (root == null) {
				return res;
			}
			Traversal(res,root);
			//Traversal2(res,root);
			return res;
		}
	}

	public static void main(String[] args) {
	}

}
