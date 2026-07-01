class MinStack:

    def __init__(self):
        self.stack=deque()
        self.minstack=float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.minstack=val
            self.stack.append(val)
        else:
            if val < self.minstack:
                # Push the encoded value, update tracker to actual new min
                self.stack.append(2 * val - self.minstack)
                self.minstack = val
            else:
                self.stack.append(val)
    def pop(self) -> None:
        a=self.stack.pop()
        if(a<self.minstack):
            self.minstack=2*self.minstack-a

    def top(self) -> int:
        a=self.stack[-1]
        if(a<self.minstack):
            return self.minstack
        return a

    def getMin(self) -> int:
        return self.minstack