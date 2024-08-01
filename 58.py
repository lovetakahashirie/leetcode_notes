class Solution:
  def lengthOfLastWord(self, s: str) -> int:
#   每到' ' 就reset length, 爲了節省時間，從後面開始
    i = len(s)-1 # start from last index
    length = 0 # start from 0
    
    while s[i]==' ':
      i -= 1 # if space then move left
      
    while i>=0 and s[i]!=' ':
      i -= 1
      length += 1
    return length
