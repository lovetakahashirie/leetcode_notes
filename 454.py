class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        total = 0
        dict12 = {}

        # 先count每個1X2每個出現的次數
        for i1 in nums1:
            for i2 in nums2:
                dict12[0-i1-i2] = dict12.get(0-i1-i2, 0) +1

        # 如果 == 3X4，那就total+=count
        for i3 in nums3:
            for i4 in nums4:
                if i3+i4 in dict12:
                    total += dict12[i3+i4]

        return total
