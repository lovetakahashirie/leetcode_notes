class MyQueue:

    def __init__(self):
       self.stackin = [] 
       self.stackout = []

    # think of this  <-out][in->
    def push(self, x: int) -> None:
        self.stackin.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        if self.stackout == []:
            while self.stackin != []:
                self.stackout.append(self.stackin.pop())
        return self.stackout.pop()
            

    def peek(self) -> int:
        if self.empty():
            return None
        if self.stackout == []:
            while self.stackin != []:
                self.stackout.append(self.stackin.pop())
        return self.stackout[-1]

    def empty(self) -> bool:
        if self.stackin == [] and self.stackout == []:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
