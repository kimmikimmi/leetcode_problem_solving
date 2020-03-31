class Solution:
    def isValid(self, s: Str) -> bool:
        stack = []
        start = ['(', '{', '[']
        pairs = {'[': ']', '{': '}', '(': ')'}

        for elem in s:
            if elem in start:
                stack.append(elem)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if pairs[top] != elem:
                    return False    
        
        if len(stack) == 0:
            return True            
        return False                    