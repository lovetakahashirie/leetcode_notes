# 先set for loop走完全部n個，所以一定是range len
# 先set個index，從0開始
# 當我需要remove時，就pop(index)再後面append一個_。但由於我pop了，所以下輪我也要check同一個index位，i不變。如果我這輪不用pop，就i++，因爲下一輪要check左一格
# 最後要return有多少個!=val的，return i就可以，因爲移了多少格就代表有多少個!=val


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for _ in range(len(nums)):
            if nums[i]==val:
                nums.pop(i)
                nums.append('_')
            else:
                i+=1
        return i
