class Solution:
    def longestPalindrome(self, s: str) -> int:

        seen=set()
        length=0

        for i in s:
            if i in seen:
                seen.remove(i)
                length+=2
            else:

                seen.add(i)
        
        if seen:
            length+=1

        return length