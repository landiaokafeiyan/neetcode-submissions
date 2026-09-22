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