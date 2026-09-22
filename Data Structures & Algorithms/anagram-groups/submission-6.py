# #I do not need to compare every pair of strings with a helper function. Instead, I create a canonical key for each word.

# For every string, I sort its characters and convert the result back into a string. All anagrams produce the same sorted string, so I use that sorted string as the key in a hash map.

# The value for each key is a list of the original words that share that key. After processing all words, I return all the values in the hash map.

# If there are n strings and the maximum word length is k, the time complexity is O(n × k log k), because I sort every word. The space complexity is O(n × k) for storing the grouped strings and keys.

# I do not need a helper function to compare pairs of strings. Instead, I map every word to a canonical representation.

# For each word, I sort its characters once and use the resulting string as a hash-map key. Since anagrams have the same sorted characters, they produce the same key and are appended to the same list.

# This avoids repeatedly comparing a word against existing groups. Each word is processed once, followed by an average O(1) hash-map lookup.


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