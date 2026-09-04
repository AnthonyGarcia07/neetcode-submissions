class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = {}
        l = 0
        longest = 0

        for r in range(len(s)):
            char_freq[s[r]] = char_freq.get(s[r], 0) + 1

            while ((r - l) + 1) - max(char_freq.values()) > k:
                char_freq[s[l]] -= 1
                l += 1

            longest = max(longest, (r - l) + 1)
        return longest