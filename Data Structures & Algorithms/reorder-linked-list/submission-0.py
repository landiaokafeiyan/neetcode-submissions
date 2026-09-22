# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Find Middle + Reverse + Merge
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # 1. Find middle
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Split into two lists
        second = slow.next
        slow.next = None

        # 3. Reverse second half
        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        second = prev

        # 4. Merge two lists alternately
        first = head

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2