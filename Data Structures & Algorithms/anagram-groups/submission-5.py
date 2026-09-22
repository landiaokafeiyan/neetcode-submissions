class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}  # key: 排序后的字符串 (str), value: 异位词列表 (list)
        
        for s in strs:
            # 1. 排序并转为字符串作为不可变的 key
            key = "".join(sorted(s))
            
            # 2. 如果 key 不在字典中，先初始化一个空列表 第一次出现需要初始化一个list
            if key not in seen:
                seen[key] = []
                
            # 3. 将原字符串追加到列表中
            seen[key].append(s)
            
        # 4. 返回所有分组的 values
        return list(seen.values())