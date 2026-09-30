class MyHashSet:

    def __init__(self):
        self.data = []#最简单的方法就是使用list 来存储数据表示数据 这里只是关注key 但是没有key 对应的value 怎么能说是hash set呢 怎么定义haseset hashset 有哪些性质

    def add(self, key: int) -> None:
        if key not in self.data:
            self.data.append(key)

    def remove(self, key: int) -> None:
        if key in self.data:
            self.data.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.data
# 功能正确的 HashSet 简化实现，但它实际上是用 Python List 模拟 Set，并没有实现 Hashing。add() 先检查是否存在，因此不会添加重复元素；remove() 在元素存在时才删除；contains() 返回一个布尔值。
# 但是你使用的底层数据结构是 List。如果两个不同的 key 被映射到同一个 bucket，就会产生 Hash Collision（哈希冲突）。我们可以用 Linked List 来保存同一个 bucket 中的多个 key。current implementation requires a linear scan, whereas a well-designed hash table can achieve constant-time operations on average
        #Set 是抽象数据类型，HashSet 是基于哈希表的实现，而 Linked List 可以用于解决哈希冲突。
# Python 的 dict 和 set 都是内置的哈希表实现。普通 list 的 in 操作通常需要线性扫描，时间复杂度为 O(n)。
# 在这道题中，我们可以使用 Array + Hash Function + Linked List 实现真正的 HashSet，而不是只用一条链表保存所有元素。Python provides built-in hash-based data structures such as dictionaries and sets. However, this problem requires us to implement a HashSet without using them.
# A simple list-based solution would require a linear scan for membership checks, resulting in O(n) time complexity.
# Instead, I use an array of buckets and a hash function to map each key to a bucket. Each bucket contains a linked list to handle hash collisions through separate chaining.
# # With a good hash distribution and a controlled load factor, insertion, deletion, and lookup take O(1) time on average.

class ListNode:
    def __init__(self, key: int):
        self.key = key
        self.next = None# Check duplicates before insertion
# 为什么 add、remove 和 contains 都从 cur.next 开始
class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for _ in range(10**4)]#这句创建了 10,000 个 bucket，每个 bucket 都包含一个 Dummy Node。这里的 ListNode(0) 只是占位节点。它的 key=0 并不代表 HashSet 已经包含元素 0。
# 真正的元素都从 dummy.next 开始。它创建了一个长度为 10,000 的 Python List，每个元素都是一个独立的 ListNode(0)。每个节点代表一个 bucket 的 Dummy Node

    def add(self, key: int) -> None:#检查重复，然后在尾部插入Traverse → Check duplicate → Insert at tail
        cur = self.set[key % len(self.set)]#key % len(self.set) 是什么？
# 这是 Hash Function，用于计算 key 对应的 bucket 索引。I compute the bucket index using the modulo hash function, then initialize cur to the dummy head of the corresponding linked list. This allows me to traverse the bucket and perform insertion, lookup, or deletion.
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:#你并没有让 cur 指向需要删除的节点，而是让它始终停在目标节点的前一个节点。
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:#只遍历，不修改链表
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)