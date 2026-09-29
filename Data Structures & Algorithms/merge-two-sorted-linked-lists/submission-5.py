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
                tail.next = list1#存
                list1 = list1.next#改
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next#移动

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next

# We’re given two sorted linked lists, and we need to merge them into one sorted list.
# The key property is that both input lists are already sorted.A straightforward approach would be to traverse both lists, collect all values into an array, sort the array, and then rebuild a linked list.If the two lists contain n and m nodes, sorting would take O((n+m) log(n+m)) time, and we would also need O(n+m) extra space.But that approach throws away the fact that both lists are already sorted.
# Since each list is sorted, at any moment the smaller of the two current head nodes must be the next node in the merged result.So I can use two pointers, one for each list.
# I’ll also use a dummy node to simplify construction of the result list, and a tail pointer that always points to the last node in the merged list.While both lists still have nodes, I compare list1.val and list2.val.
# If list1.val is smaller, I connect tail.next to list1, advance list1, and then move tail forward.
# Otherwise, I do the same with list2.Once one list is exhausted, I don’t need to compare anymore because the remaining part of the other list is already sorted. So I can attach the entire remaining list directly to tail.next.Each node is visited once, so the time complexity is O(n+m).
# Since I reuse the existing nodes and only keep a few pointers, the extra space is O(1).

