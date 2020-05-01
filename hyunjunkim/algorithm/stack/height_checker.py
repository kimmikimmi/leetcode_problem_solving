from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        final = sorted(heights)
        cnt = 0
        for i in range(len(heights)):
            if final[i] != heights[i]:
                cnt = cnt + 1

        return cnt                

        
a = Solution()
print(a.heightChecker([1,1,4,2,1,3]))