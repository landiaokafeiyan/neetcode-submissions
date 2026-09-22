
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
#First, I would check whether the two strings have different lengths. If they do, they cannot be anagrams, so I return `False` immediately.

# Otherwise, I sort both strings and compare the sorted results. If two strings are anagrams, they contain exactly the same characters with the same frequencies, so their sorted character sequences must be identical.

# The time complexity is O(n log n), because sorting each string dominates the runtime. The space complexity is O(n) in Python because `sorted` creates new lists.

# Can you solve it in O(n) time without sorting?

#Yes. Since the strings contain lowercase English letters, I can count the frequency of each character instead of sorting.

# I would first return `False` if the strings have different lengths. Then I would use two hash maps: one records the character frequencies in `s`, and the other records the frequencies in `t`.

# After counting both strings, I compare the two frequency maps. If every character has the same frequency in both strings, they are anagrams.

# This takes O(n) time because I scan each string once. The space complexity is O(1) if the input is restricted to the 26 lowercase English letters, since the number of possible keys is bounded by a constant. More generally, it is O(k), where k is the number of distinct characters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
#use hash map for each or a hash table to count all the 26 characters
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
# use one hashmap
# I use one hash map as a frequency balance. First, I add one for every character in s. Then I subtract one for every character in t. If any count becomes negative, t contains that character more times than s, so the strings cannot be anagrams. Since the strings have the same length, if no count is negative, all counts must end at zero, and the strings are anagrams.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            count[char] = count.get(char, 0) - 1
            if count[char] < 0:
                return False

        return True
                