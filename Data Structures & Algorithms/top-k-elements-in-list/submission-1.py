
import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. 统计频次
        count = Counter(nums)
        
        # 2. 维护大小为 k 的小顶堆
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
                
        # 3. 直接提取堆中的元素返回
        return [num for freq, num in heap]
#    Hash 是使用频率最高、用处最广的数据结构之一。它的核心灵魂在于：利用空间换时间，将查找、插入、删除的时间复杂度降到 $O(1)$     
# 存储载体：就是普通的 Python list（列表）
# Python 中并没有专门的“Heap 数据结构对象”。任何一个普通的 list，只要它的元素排列顺序满足堆的性质，它就是一个堆。

# heapq 并不是类（Class），而是一个模块（Module）
# heapq 实际上是 Python 标准库中的一个模块（包含一系列纯函数），而不是一个 class。

# 你不需要也不应该像这样去实例化它：h = heapq() ❌

# 你只需要传入一个原生的 list 作为第一个参数，调用它的函数即可：heapq.heappush(my_list, item)  heapq.heappop(my_list)
# 不可变对象 (Immutable) 才能做 Key：int, float, str, tuple, bool
# 可变对象 (Mutable) 不能做 Key：list, dict, set ❌（因为值改变后 Hash 值会变，导致再也找不回该元素）。
# 在设计 HashMap 求解算法前，永远先明确：字典的 Key 存什么（用来做条件匹配）？Value 存什么（用来作为最终答案返回）？
# 需要将列表作为 Key 时（如统计坐标 [x, y]），必须转换为不可变元组 tuple([x, y])。
# collections.Counter：自带计数的简化版 dict。

# collections.defaultdict：自动处理 Key 不存在时的初始化（如 defaultdict(list)）