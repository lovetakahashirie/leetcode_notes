class Queue:
    def __init__(self):
        self.q = collections.deque()

    def push(self, index: int, k: int, nums: List[int]) -> int:
        if not self.q: # empty
            self.q.append(index)
            return nums[index]
        else:
            if nums[self.q[0]] <= nums[index]: # if max<=curVal
                self.popAll()
                self.q.append(index)
                return nums[index]
            else:
                while nums[self.q[-1]] <= nums[index]: # 不然就要放後面
                    self.q.pop()
                self.q.append(index)
                
                if index-self.q[0] >= k: # 最後處理first出index未
                    self.q.popleft()
                    return nums[self.q[0]]
                else:
                    return nums[self.q[0]]

    def popAll(self) -> None:
        while self.q:
            self.q.pop()
            

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = Queue()
        output = []
        for index in range(len(nums)):
            output.append(dq.push(index, k, nums))
        return output[k-1:]
