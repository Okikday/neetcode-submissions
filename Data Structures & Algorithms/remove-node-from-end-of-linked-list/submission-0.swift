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
        let tail = reverseNode(head!)
        var l: ListNode? = nil
        var r = tail

        var c = 1
        while c < n{
            l = r
            r = r?.next
            c += 1
        }

        if l != nil{
            l?.next = r?.next
        }
        
        return reverseNode(l == nil ? r!.next : tail!)

    }

    func reverseNode(_ node: ListNode?) -> ListNode?{
        var tail: ListNode? = nil
        var curr = node
        while curr != nil{
            var next = curr?.next
            curr?.next = tail
            tail = curr
            curr = next
        }
        return tail
    }
}