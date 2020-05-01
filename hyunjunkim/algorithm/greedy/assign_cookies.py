from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        current = 0
        for i in range(0, len(s)):
             g[current] = g[current] - s[i]
             if g[current] <= 0:
                 g[current] = 0
                 current = current + 1

             if current == len(g):
                return current
        return current

a = Solution()
print(a.findContentChildren([1,2,3], [1,1]))
