from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # 访问成功后，移到最右端，成为最近使用
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 旧 key 被更新，也算最近使用
            self.cache.move_to_end(key)

        self.cache[key] = value

        if len(self.cache) > self.cap:
            # 删除最左端，即最久未使用的 key-value
            self.cache.popitem(last=False)


# In Python, I can use an OrderedDict, which supports O(1) lookup, moving an accessed key to the most-recent end, and removing the least-recent key. Therefore, both get and put are O(1). If built-in ordered containers are not allowed, I would implement the same behavior with a hash map from keys to nodes and a doubly linked list that maintains recency order.

class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity

        # key -> Node
        self.cache = {}

        # dummy nodes：避免删除头尾节点时的特殊情况
        self.head = Node()  # head.next 是 LRU
        self.tail = Node()  # tail.prev 是 MRU

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        # node 前后一定有节点，因为真实节点夹在 dummy head/tail 中间
        previous = node.prev
        following = node.next

        previous.next = following
        following.prev = previous

    def _insert_mru(self, node: Node) -> None:
        # 插入 tail 前，使 node 成为最近使用
        previous_mru = self.tail.prev

        previous_mru.next = node
        node.prev = previous_mru

        node.next = self.tail
        self.tail.prev = node

    def _move_to_mru(self, node: Node) -> None:
        self._remove(node)
        self._insert_mru(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # 被访问，所以更新为最近使用
        self._move_to_mru(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 更新已有 key：更新 value，再移到最近使用位置
            node = self.cache[key]
            node.value = value
            self._move_to_mru(node)
            return

        # 新 key：创建节点，加入字典和链表
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._insert_mru(new_node)

        # 超过容量时，删除最久未使用节点
        if len(self.cache) > self.capacity:
            lru_node = self.head.next

            self._remove(lru_node)
            del self.cache[lru_node.key]