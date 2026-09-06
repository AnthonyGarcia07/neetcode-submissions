class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, window = {}, {} # frequency hashmaps

        # Count the frequency of each character required from t
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # have = requirements satisfied, need = total unique requirements (counts the keys at hashmap countT)
        # res stores the best [left, right] indices; resLen stores its length
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0

        # Move the right pointer through s and add each character to the window
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # If the current character c is required by t, and its frequency in window has just reached the frequency required by countT,
            # increment have by 1.
            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""