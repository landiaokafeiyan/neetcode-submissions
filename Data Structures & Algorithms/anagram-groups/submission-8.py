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
            key = "".join(sorted(s))#Group Anagrams without sorting :Instead of sorting each word, I use a 26-element frequency array as its signature.I convert the array to a tuple 

                
            
            # 2. 如果 key 不在字典中，先初始化一个空列表 第一次出现需要初始化一个list
            if key not in seen:
                seen[key] = []
                
            # 3. 将原字符串追加到列表中
            seen[key].append(s)
            
        # 4. 返回所有分组的 values
        return list(seen.values())


from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}  # key: 26-letter frequency tuple, value: matching words

        for word in strs:
            count = [0] * 26

            # Build the frequency signature for this word.
            for char in word:
                index = ord(char) - ord("a")
                count[index] += 1

            # A list is mutable, so convert it to an immutable tuple for a dict key.
            key = tuple(count)

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())



#         My first solution uses a hash map to group words by their sorted characters.

# For each word, I sort its characters and use the sorted result as the hash-map key. Since all anagrams have exactly the same characters, they produce the same key and are collected in the same list.

# If there are n words and the maximum word length is k, the time complexity is O(n × k log k), because I sort every word. The auxiliary space is O(n × k) for the hash map, keys, and output groups.

# This solution is simple, readable, and works for arbitrary characters.
# We can improve the key construction when the input contains only lowercase English letters.

# Instead of sorting each word, I create a frequency array of length 26. For every character, I map it to an index from 0 to 25 using `ord(char) - ord("a")` and increment its count. I then convert the array to a tuple and use that tuple as the hash-map key.

# Anagrams have identical frequency tuples, so they are grouped together.

# The time complexity is O(n × k), because each character is processed once. The 26-element tuple conversion is O(26), which is constant. The auxiliary space per key is O(1), since the alphabet size is fixed.
# The sorting solution is more general and easier to implement. I would choose it when the character set is unrestricted or when clarity is the main priority.

# The frequency-array solution is faster because it avoids sorting, but it relies on the assumption that the input contains only lowercase English letters. For this specific problem, I would prefer the frequency-array solution if I want the optimal O(n × k) runtime.
