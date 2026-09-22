from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        # Dictionary to store grouped anagrams
        print(f'strs={strs}')
        anagrams = defaultdict(list)
        print(f'storted={anagrams}')
        
        for word in strs:
            # Sort the word to create a key
            sorted_word = ''.join(sorted(word))
            # Append the original word to the corresponding key
            anagrams[sorted_word].append(word)
        
        # Return the values of the dictionary as a list of lists
        return list(anagrams.values())