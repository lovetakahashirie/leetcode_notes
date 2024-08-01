class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        red = {} # reverse d
        for i in nums:
            d[i] = d.get(i, 0) + 1
        
        for key,val in d.items():
            red[val] = red.get(val, []) + [key]
        
        des = sorted(list(red.keys()), reverse=True) # descending
        
        output = []
        for i in des:
            if len(output)>=k:
                break
            output += red[i]
        return output


