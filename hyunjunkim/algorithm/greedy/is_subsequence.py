class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
            
        sLen = len(s)
        sIndex = 0

        for tChar in t:
            if s[sIndex] == tChar:
                sIndex = sIndex + 1;
            if sIndex == sLen:
                return True    

        return False
        

