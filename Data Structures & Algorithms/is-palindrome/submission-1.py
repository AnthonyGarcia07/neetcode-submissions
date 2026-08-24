class Solution:
    def isPalindrome(self, s: str) -> bool:
        palin = ""

        for char in s:
            if char.isalnum():
                palin += char
            
        return palin.lower() == palin[::-1].lower()