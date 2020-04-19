from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = 0
        
        for i in range(1, len(prices)):
           if prices[i] > prices[i-1]:
               profits = profits + (prices[i] - prices[i-1])

        return profits

        
            
solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))
print(solution.maxProfit([1,2,3,4,5]))
print(solution.maxProfit([5,4,3,2,1]))