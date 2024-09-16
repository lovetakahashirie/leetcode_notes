# 要知道這是一個循環的機制，如何到10了就下一個，全部都10了就1加在前面

# 做法：首先set index從最後開始
# 當i還在list valid index裏面，我就將i所在的位置+1
# 然後check，如果i位!=10，那就不用進位，直接return
# 如果i位==10，那就要先將i位=0，i--
# 一直做到i=-1爲止（代表已經連最左邊的0位都進了，還解決不了問題）
# 那現在全部位都0了，那直接前面加個1再return就可以了


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1 # 代表最後一個index
        while i>=0:
            digits[i]+=1
            if digits[i]!=10:
                return digits
            digits[i]=0
            i-=1
        return [1]+digits
