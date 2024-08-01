class MyStack:

    def __init__(self):
        self.q = deque()
        # from collections import deque, which is queue in python

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())
        return self.q.popleft()


    def top(self) -> int:
        if self.empty():
            return None
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())
        top_ = self.q.popleft()
        self.q.append(top_)
        return top_

    def empty(self) -> bool:
        if len(self.q) ==0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
