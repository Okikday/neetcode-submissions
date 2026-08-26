/**
 * Definition for singly-linked list.
 * class ListNode {
 *     var val: Int
 *     var next: ListNode?
 *     init(_ val: Int) {
 *         self.val = val
 *         self.next = nil
 *     }
 * }
 */

class Solution {
    func mergeTwoLists(_ list1: ListNode?, _ list2: ListNode?) -> ListNode? {
        if list1 == nil || list2 == nil{
            return list1 ?? list2
        }
        
        var head: ListNode? = nil, l = list1, r = list2, curr: ListNode? = nil
        
        if l!.val >= r!.val{
            curr = r; head = r; r = r?.next;
        }else{
            curr = l; head = l; l = l?.next;
        }

        while l != nil && r != nil{
            if r!.val >= l!.val{
                curr?.next = l; l = l?.next;
            }else{
                curr?.next = r; r = r?.next;
            }
            curr = curr?.next
        }
        
        curr?.next = l ?? r
        return head
    }
}
