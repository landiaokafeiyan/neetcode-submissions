import heapq


class MedianFinder:

    def __init__(self):
        # small 保存较小的一半
        # Python 只有 min heap，所以存负数模拟 max heap
        self.small = []

        # large 保存较大的一半
        self.large = []

    def addNum(self, num: int) -> None:
        # 1. 先把 num 放入 small
        heapq.heappush(self.small, -num)

        # 2. 保证 small 里的所有数字 <= large 里的所有数字
        #
        # small 最大值 = -self.small[0]
        # large 最小值 = self.large[0]
        if (
            self.large
            and -self.small[0] > self.large[0]
        ):
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        # 3. 平衡两个 heap 的大小
        #
        # 我们允许 small 比 large 多一个
        if len(self.small) > len(self.large) + 1:
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        elif len(self.large) > len(self.small):
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)

    def findMedian(self) -> float:
        # 奇数个数字
        if len(self.small) > len(self.large):
            return -self.small[0]

        # 偶数个数字
        return (-self.small[0] + self.large[0]) / 2