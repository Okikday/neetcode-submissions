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
    func hasCycle(_ head: ListNode?) -> Bool {
        if head == nil{return false}
        var slow = head, fast = head

        while fast?.next != nil{
            slow = slow?.next
            fast = fast?.next?.next

            if slow === fast{
                return true
            }
        }

        return false
        
    }
}