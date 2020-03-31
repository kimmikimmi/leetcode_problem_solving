class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)

        if not self.minStack: #list is empty
            self.minStack.append(x)
        else:
            current = min(self.minStack[-1], x)
            self.minStack.append(current)
            


    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()

obj.push(2)
obj.push(4)
obj.push(1)
obj.push(3)
obj.pop()
obj.pop()

# obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(obj.stack)
print(obj.minStack)
print(param_3)
print(param_4)