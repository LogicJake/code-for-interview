package nowcoderV1;

import java.util.ArrayList;

/*
 * ����һ������������ֵ��β��ͷ��˳�򷵻�һ��ArrayList��
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
	 * �ͷ���������
	 * �½�ͷָ�룬�������������ڵ���뵽�µ�ͷָ��ĺ��棬������˷���
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
