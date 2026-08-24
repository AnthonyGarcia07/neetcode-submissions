class Solution:
    def isPalindrome(self, s: str) -> bool:
        palin = ""

        for char in s:
            if char.isalnum():
                palin += char.lower()
            
        return palin == palin[::-1]