class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            leftover = target - nums[i] # 先計算我這個num要pair with什麽
            if leftover in d: # 如果在裏面
                return [i, d[leftover]] # return both index
            d[nums[i]] = i # 如果不在就把自己的資料放進去
            
        # 2n
        # for num, index1 in zip(nums, range(len(nums))):
        #     # {'left number': index}
        #     d[target-num] = index1

        # for num, index2 in zip(nums, range(len(nums))):
        #     if num in d.keys() and index2 != d[num]:
        #         return [d[num], index2]

        # n
