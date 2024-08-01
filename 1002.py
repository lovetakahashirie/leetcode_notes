class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        base = collections.Counter(words[0])

        for i in range(1, len(words)):
            # 用了&后，if >0 保證每個word都有出現過一次那個字母
            base = base & collections.Counter(words[i]) # 注意：& 是每個拿min，and是拿max

        duplicateList = []
        for i in base: # for eachkey in counter obj
            while base[i]>0: # value>0
            # 要用while，不能用if，因爲要append到value=0，代表已經append了（出現過）n此
                duplicateList.append(i)
                base[i] -= 1

        return duplicateList




