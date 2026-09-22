# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Find Middle + Reverse + Merge
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
# I split the list at the midpoint, reverse the second half so that the tail nodes become accessible from the front, and then merge the two halves alternately.
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
            temp2 = second.next#Merge 时也要先保存两个 next下面马上要修改

            first.next = second#修改 next 之前，先保存原来的 next
            second.next = temp1

            first = temp1
            second = temp2