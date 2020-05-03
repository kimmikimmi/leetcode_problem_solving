from typing import List
'''
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.

Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]
 
Note:

1 <= arr.length <= 10000
0 <= arr[i] <= 9
'''
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        stack = []
        for e in arr:
            if e == 0:
                stack.append(0)
            stack.append(e)
        print(stack[:len(arr)])    
        
        for i in range(len(arr)):
            arr[i] = stack[i]

a = Solution()
arr = [1,2,3,0,4,0,5]

a.duplicateZeros(arr)
print(arr)
        