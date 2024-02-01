/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode mk=new ListNode(0);
        ListNode temp=mk;
        int carry=0;
        int n1,n2,sum;
        while( l1!=null || l2!=null || carry!=0 ){
            if (l1!=null){
                 n1=l1.val;
            }else{
                  n1=0;
            }
            if (l2!=null){
                 n2=l2.val;
            }else{
                 n2=0;
            }
             sum=n1+n2+carry;
            carry=sum / 10;
            sum=sum % 10;
            ListNode news=new ListNode(sum);

            temp.next=news;
            if(l1!=null){
                 l1=l1.next;
            }
            if(l2!=null){
                 l2=l2.next;
            }
            temp=temp.next;
        }
        return mk.next;
    }
}
