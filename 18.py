class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        output = []
        for k in range(n):
            if nums[k] > target/4:
                break
            if k>0 and nums[k]==nums[k-1]:
                continue
            
            for i in range(k+1, n):
                if nums[i]>(target-nums[k])/3:
                    break
                if i>k+1 and nums[i]==nums[i-1]:
                    continue
                
                left = i+1
                right = n-1

                while left<right:
                    sums = nums[k]+nums[i]+nums[left]+nums[right]
                    if sums<target:
                        left+=1
                    elif sums>target:
                        right-=1
                    else: # ==
                        output.append([nums[k],nums[i],nums[left],nums[right]])
                        while left<right and nums[left]==nums[left+1]:
                            left+=1
                        while left<right and nums[right]==nums[right-1]:
                            right-=1
                        left+=1
                        right-=1

        return output
