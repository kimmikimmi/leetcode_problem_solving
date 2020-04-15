class Solution(object):
    def climbStairs(self, n):
        
        stairCache = [1] * (n + 1)
        for i in range(2, n + 1):
            stairCache[i] = stairCache[i-1] + stairCache[i-2]
        return stairCache[n]


a = Solution()
print(a.climbStairs(3))

