class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:

            while l < r and not s[l].isalnum():
                l += 1

            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True
        # Let me first restate the problem to make sure I understand it correctly.
# We are given a string, and we need to determine whether it is a palindrome after ignoring non-alphanumeric characters and ignoring case. In other words, we only compare letters and digits, and the comparison should be case-insensitive.For the constraints, the input is a string of length \(n\). I want to avoid building an unnecessary extra string if possible, because this problem can be solved in linear time and constant extra space.My first thought is to use two pointers. I can place one pointer at the beginning of the string and one at the end. Then I move them toward each other.Before comparing the two characters, I skip any character that is not alphanumeric. So the left pointer keeps moving right until it reaches a valid character, and the right pointer keeps moving left until it reaches a valid character.Once both pointers are pointing to valid characters, I compare their lowercase versions. If they are different, I can immediately return false.If they match, I move both pointers inward and continue. If the two pointers meet or cross without finding a mismatch, then the string is a valid palindrome.Each character is visited at most once by either pointer, so the time complexity is O(n). I only use two pointer variables, so the extra space complexity is O(1).