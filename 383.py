class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 這個會更快，因爲有些check到某個char知道不行就false了
        for char in set(ransomNote):
            if magazine.count(char) < ransomNote.count(char):
                return False
        return True

        # 這個是一次記完全部東西，然後一次對比全部，如果有cover不了的就是false
        # if len(magazine) < len(ransomNote):
        #     return False
        
        # counter = {}
        # for r in ransomNote:
        #     counter[r] = counter.get(r, 0) +1
        # for m in magazine:
        #     counter[m] = counter.get(m, 0) -1

        # if max(counter.values())<=0:
        #     return True
        # else:
        #     return False

