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
    func reverseList(_ head: ListNode?) -> ListNode? {
        if head == nil{
            return nil
        }
        var tail: ListNode? = nil
        var curr = head
        while curr != nil{
            let next = curr?.next // 2, 3
            curr?.next = tail // 0
            tail = curr // 1,0
            curr = next // 2, 3

        }
        return tail
    }
}
