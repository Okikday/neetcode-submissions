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
    func reorderList(_ head: ListNode?) {
        var slow = head, fast = head?.next

        // Split them into two using fast and slow
        while fast?.next != nil{
            slow = slow?.next
            fast = fast?.next?.next
        }
        // slow points at the middle, fast points at the end atp

        
        var tail: ListNode? = nil
        var curr = slow?.next
        slow?.next = nil

        // Reverse the second half (fast)
        while curr != nil{
            var next = curr?.next
            curr?.next = tail
            tail = curr
            curr = next
        }

        // 
        var a = head
        var b = tail
        while b != nil{
            let tmp1 = a?.next
            let tmp2 = b?.next
            a?.next = b
            b?.next = tmp1 
            a = tmp1
            b = tmp2
        }
    }
}
