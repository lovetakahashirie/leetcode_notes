class Solution:
# 1. 3pointers 比hashdict 更快
# 2. prevent a repeat, but not index0
# 3. prevent b,c repeat
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i]>0:
                return output
            if i>0 and nums[i-1]==nums[i]:
                continue

            left = i+1
            right = len(nums)-1

            while left<right:
                if nums[i] + nums[left] + nums[right] < 0:
                # 這裏不用加 while repeat就left-=1。因爲上兩行就在做一樣的事情，根本沒必要
                    left +=1
                elif nums[i] + nums[left] + nums[right] > 0:
                # 這裏不用加 while repeat就right+=1。同上
                    right -=1
                else:
                    output.append([nums[i], nums[left], nums[right]])
                    # 這次就要自己移動left right了，不然又要append duplicate
                    while left<right and nums[left]==nums[left+1]:
                        # 要加left<right，不然到最後一個會飛出去變成compare with none
                        left +=1
                    while left<right and nums[right-1]==nums[right]:
                        right-=1
                    left +=1
                    right-=1
        return output

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         output = []
#         targetList = []
        
#         if min(nums)==max(nums):
#             if nums[0]==0:
#                 return [[0,0,0]]
#             else:
#                 return [] # all >0 or <0

#         for num in nums:
#             targetList.append(0-num)
        
#         for target, i in zip(targetList, range(len(targetList))):

#             # just two sum question in LC1
#             d = {}
#             for num, j in zip(nums, range(len(nums))):
#                 if i==j: continue # repeat use

#                 complement = target - num # what i want to find
#                 if complement in d:
#                     output.append(sorted([0-target, num, complement]))
#                 else:
#                     d[num] = j

#         return list(set(tuple(x) for x in output))
#         # 難度在remove duplicate in list，很耗時
#         # cant set(list) because can change ==> not hashable ==> change to immutable ==> use tuple
