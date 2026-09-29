# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val<=list2.val:
            list1.next=self.mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next=self.metgeTwoLists(list1,list2.next)
            return list2
            # Time: O(n + m)
# Space: O(n + m)注意这里空间不是 O(1)，因为 recursion stack 最坏可能有 n+m 层
# A brute-force approach would be to extract all values from both lists, sort them, and rebuild a linked list. That would take O((n+m) log(n+m)) time and O(n+m) extra space.
# But since both lists are already sorted, we can do better. I can maintain two pointers, compare the current nodes, append the smaller one to the result, and advance that pointer. Each node is visited exactly once, so the time complexity becomes O(n+m). Using an iterative approach with a dummy node, the extra space is O(1).
# Since both linked lists are already sorted, sorting everything again is unnecessary.已排序输入意味着通常不需要重新排序，可以用双指针做 linear merge。
class Solution:#用 iterative + dummy 重写一遍，四步还记得吧：dummy 开头 → while 里比较摘小 → 接上剩余 → return dummy.next。
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next
