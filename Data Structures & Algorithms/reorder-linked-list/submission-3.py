# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# prev = None
# curr = head

# while curr:
#     nxt = curr.next
#     curr.next = prev
#     prev = curr
#     curr = nxt   
# Reorder a linked list in-place.

# 不要马上写代码。

# 你应该先说：

# “I see this as three linked-list operations. First, I need to find the middle using a slow and fast pointer. Then I reverse the second half of the list. Finally, I merge the two halves by alternating nodes.”         
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # 1. Find middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse second half
        second = slow.next
        slow.next = None

        prev = None

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # 3. Merge two halves
        first = head
        second = prev

        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next
        