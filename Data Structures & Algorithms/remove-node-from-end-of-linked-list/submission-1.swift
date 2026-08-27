/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */
class Solution {
    func removeNthFromEnd(_ head: ListNode?, _ n: Int) -> ListNode? {
        if head == nil{return nil}
        let dummy: ListNode? = ListNode(0)
        dummy?.next = head
        var l = dummy
        var r = head
        var c = n

        while c > 0{
            r = r?.next
            c -= 1
        }

        while r != nil{
            l = l?.next
            r = r?.next
        }

        l?.next = l?.next?.next
        return dummy?.next
    }

}