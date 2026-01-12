class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        nums = []
        for i in str(num):
            nums.append(i)
        for i in nums:
            if num % int(i) == 0:
                count+=1
        return count


        