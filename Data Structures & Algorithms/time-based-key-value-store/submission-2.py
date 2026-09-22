class TimeMap:
# 所以 TimeMap 最关键的设计思想是：

# 我们不是要做 exact lookup，而是要做 predecessor search：找 <= target 的最大 timestamp。

# 正因为如此，有序 list + binary search 比普通 nested dictionary 更合适。
    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = {}#这里定义成dictionary了
        if timestamp not in self.keyStore[key]:
            self.keyStore[key][timestamp] = []
        self.keyStore[key][timestamp].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyStore:
            return ""
        seen = -1

        for time in self.keyStore[key]:
            if time <= timestamp:
                seen = max(seen, time)
        return "" if seen == -1 else self.keyStore[key][seen][-1]

#最优的方法是定义成list of list 因为list是自然排序 可以binary search
class TimeMap:

    def __init__(self):
        self.keyStore = {}  # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])#那么 self.keyStore[key] 是一个 list

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res