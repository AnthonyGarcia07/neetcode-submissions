class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        longest = 0
        l = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
                
            
            char_set.add(s[r])
            longest = max(longest, (r - l) + 1)

        return longest

# The right pointer expands the window one character at a time. If the new character is already inside the window, move the left pointer forward while removing characters from the set until that duplicate is gone. Then add the current character and calculate the window's length. Because every window we measure contains only unique characters, and the right pointer eventually examines every character, we find the longest valid substring.