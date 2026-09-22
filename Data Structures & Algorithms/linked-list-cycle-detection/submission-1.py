# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:#只要 fast 还没有到链表边界，并且它后面还有一个节点，我就可以让 fast 再走两步。
            slow = slow.next
            fast = fast.next.next
            if slow == fast:#两个 pointer 是否指向同一个 Node 对象
                return True
        return False