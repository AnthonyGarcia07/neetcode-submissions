class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Get the string lengths
        n1 = len(s1)
        n2 = len(s2)
        
        # s1 = "abcd"    length 4
        # s2 = "abc"     length 3
        # there can't possibly be a length-4 substring inside a length-3 string.
        if n1 > n2:
            return False

        # store character frequencies
        s1_counts = [0] * 26
        s2_counts = [0] * 26


        for i in range(n1):
            # Increase the frequency of this character by 1
            s1_counts[ord(s1[i]) - 97] += 1
            s2_counts[ord(s2[i]) - 97] += 1
  
        # If they're equal, then they must be permutations
        if s1_counts == s2_counts:
            return True
        
        # This is the actual fixed sliding window
        # 1st for loop has already proccessed n1
        for i in range(n1, n2):
            # Add the new character entering from the right.
            s2_counts[ord(s2[i]) - 97] += 1
            # Remove the old character leaving from the left.
            s2_counts[ord(s2[i-n1]) - 97] -= 1
            if s1_counts == s2_counts:
                return True

        return False