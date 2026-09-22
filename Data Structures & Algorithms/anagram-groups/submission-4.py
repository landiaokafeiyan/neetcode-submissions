from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[str]:
        # 使用 defaultdict，如果 key 不存在会自动初始化为空列表 []
        ans = defaultdict(list)
        
        for s in strs:
            # 将字符串排序后作为 key（因为 sorted 返回列表，需要 join 拼回字符串）
            sorted_str = "".join(sorted(s))
            # 直接将原字符串 append 到对应 key 的列表中
            ans[sorted_str].append(s)
            
        return list(ans.values())
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[str]:
        ans = defaultdict(list)
        
        for s in strs:
            # 建立长度为 26 的频次数组
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            # Python 中列表不能做 dict 的 Key，必须转成不可变的 tuple
            ans[tuple(count)].append(s)
            
        return list(ans.values())
    # $$\text{题目要查什么？} \longrightarrow \text{把用于快速查找的条件设为 Key} \longrightarrow \text{把最终需要获取的数据设为 Value}$$