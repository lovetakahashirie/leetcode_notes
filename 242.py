class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countdict = {}
        for i, j in zip(s,t):
            # 一加一減，最後全部key==0就代表
            countdict[i] = countdict.get(i, 0) + 1
            countdict[j] = countdict.get(j, 0) - 1
        
        return all(value==0 for value in countdict.values())
