class Solution:
    def isHappy(self, n: int) -> bool:
        record = set()
        while n!=1:
            strN = str(n)
            sum = 0
            for digit in strN:
                sum += int(digit)**2
            if sum in record:
                return False
            else:
                record.add(sum)
            n = sum
        return True
