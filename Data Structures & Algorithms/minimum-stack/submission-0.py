class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val) # actual stack

        if not self.minStack:
            curr_min = val
        else:
            curr_min = min(val, self.minStack[-1])

        self.minStack.append(curr_min)

    def pop(self) -> None:
        self.stack[-1:] = []
        self.minStack[-1:] = []

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
