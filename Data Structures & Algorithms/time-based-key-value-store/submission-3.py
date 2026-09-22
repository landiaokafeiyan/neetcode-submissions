# I’ll use a hash map where each key maps to a list of (timestamp, value) pairs.

# The important observation is that, for each key, calls to set arrive in increasing timestamp order. Therefore, I can simply append each new record to that key’s list.

# For get(key, timestamp), I do not need an exact timestamp match. I need the value associated with the largest stored timestamp that is less than or equal to the requested timestamp. Since the list is sorted by timestamp, I can use binary search.

# During binary search, when mid_time <= timestamp, this is a valid candidate, so I save its value and move right to look for a later valid timestamp. Otherwise, the timestamp is too large, so I move left.

# The invariant is that answer always stores the latest valid value seen so far. When the search ends, it is the value for the rightmost timestamp not exceeding the query time.



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

class TimeMap:
    def __init__(self):
        # 字典：
        # key -> [(timestamp1, value1), (timestamp2, value2), ...]
        #
        # 同一个 key 的 records 会按 timestamp 从小到大排列。
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # 第一次看到这个 key 时，先创建空列表。
        if key not in self.data:
            self.data[key] = []

        # 题目保证：同一个 key 的 timestamp 按递增顺序传入。
        # 因此直接 append 就能保持列表有序。
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # 这个 key 从未被 set 过，没有可返回的 value。
        if key not in self.data:
            return ""

        # 取出该 key 对应的、有序时间记录。
        records = self.data[key]

        left = 0
        right = len(records) - 1

        # answer 保存“目前找到的最新合法 value”。
        # 合法的意思是：record_timestamp <= 查询 timestamp。
        answer = ""

        # 标准二分：left <= right，保证最后一个候选也会被检查。
        while left <= right:
            mid = (left + right) // 2

            # 解包中间位置的 (timestamp, value)。
            mid_time, mid_value = records[mid]

            if mid_time <= timestamp:
                # 当前记录的时间不超过目标时间，所以它是合法候选。
                answer = mid_value

                # 但右侧可能存在一个“更晚但仍不超过目标”的记录，
                # 所以继续向右寻找。
                left = mid + 1

            else:
                # 当前时间太晚，mid 和其右边都不可能是答案。
                # 去左半边找更小的时间戳。
                right = mid - 1

        # 若所有记录都比目标 timestamp 晚，answer 保持为 ""。
        # 否则返回右侧最后一个合法记录的 value。
        return answer