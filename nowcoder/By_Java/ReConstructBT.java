package V1.nowcoder;

/*
 * 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
 * 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
 * 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
 */
public class ReConstructBT
{
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }
    
    public TreeNode reConstructBinaryTree(int [] pre,int [] in) {
        if(pre.length == 0 || pre == null)
            return null;
        
        TreeNode root = new TreeNode(pre[0]);
        
        if (pre.length == 1)
            return root;
            
        int rootIndex = 0;
        
        for(int i = 0; i < in.length; i++){
            if (in[i] == pre[0]){
                rootIndex = i;
            } 
        }
        
        int k = 1;
        int[] leftPre = new int[rootIndex];
        int[] leftIn = new int[rootIndex];
        int[] rightPre = new int[pre.length - rootIndex - 1];
        int[] rightIn = new int[pre.length - rootIndex - 1];
        
        int j = 0;
        for (int i = 0; i < rootIndex; i++){
            leftPre[j] = pre[k++];
            leftIn[j++] = in[i];
        }
        
        j = 0;
        for (int i = rootIndex + 1; i < in.length; i++){
            rightPre[j] = pre[k++];
            rightIn[j++] = in[i];
        } 
        
        root.left = reConstructBinaryTree(leftPre,leftIn);
        root.right = reConstructBinaryTree(rightPre,rightIn);
        return root;
    }
    
    public static void main (String[] args){
        ReConstructBT reConstructBT = new ReConstructBT();
	      int[] pre = {1,2,4,7,3,5,6,8};
	      int[] in = {4,7,2,1,5,3,8,6};
	      reConstructBT.reConstructBinaryTree(pre,in);
	  }
}
