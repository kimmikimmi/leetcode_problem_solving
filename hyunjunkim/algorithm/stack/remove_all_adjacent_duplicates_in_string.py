class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for letter in S: 
            if stack:
                top = stack[-1]
                if top == letter:
                    stack.pop()
                else:        
                    stack.append(letter)                    
            else:
                stack.append(letter)

        result = ""
        for i in stack:
            result = result + i
        return result 

a = Solution()
print(a.removeDuplicates("abbaca"))