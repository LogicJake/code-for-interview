package nowcoder;

import java.util.ArrayList;

/*
 * 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
 */
public class PrintListFromEnd {
	public class ListNode {
		int val;
		ListNode next = null;
		
		ListNode(int val) {
			this.val = val;
		}
	}
	/*
	 * 和反置链表差不多
	 * 新建头指针，遍历旧链表，将节点插入到新的头指针的后面，就完成了反置
	 */
	public ArrayList<Integer> printListFromTailToHead(ListNode listNode) {
		ArrayList<Integer> res = new ArrayList<>();
		
		while (listNode != null) {
			res.add(0, listNode.val);
			;
			listNode = listNode.next;
		}
		return res;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
	}
	
}
