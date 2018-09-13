package V1.nowcoder;

import java.util.Stack;

/* 
 * 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
 */
public class QueueByStack
{
    Stack<Integer> stack1 = new Stack<Integer>();
    Stack<Integer> stack2 = new Stack<Integer>();
    
    public void push(int node) {
        stack1.push(node);

    }
    
    public int pop() {
        while(!stack1.empty()){
            stack2.push(stack1.pop());
        }
        
        int res = stack2.pop();
        
        while(!stack2.empty()){
            stack1.push(stack2.pop());
        }
        
        return res;
    }
    
    public static void main (String[] args){
        QueueByStack queue = new QueueByStack();
        queue.push(1);
        queue.push(2);
        queue.pop();
        queue.pop();
    }
}
