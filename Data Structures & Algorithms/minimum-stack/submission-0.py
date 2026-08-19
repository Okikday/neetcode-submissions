class MinStack:

    def __init__(self):
        self.elements = list()
        self.minstack = list()

    def push(self, val: int) -> None:
        self.elements.append(val)
        
        if not self.minstack:
            self.minstack.append(val)
        else:
            if val < self.minstack[-1]:
                self.minstack.append(val)
            else:
                self.minstack.append(self.minstack[-1])

    def pop(self) -> None:
        self.minstack.pop()
        return self.elements.pop()

    def top(self) -> int:
        return self.elements[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
