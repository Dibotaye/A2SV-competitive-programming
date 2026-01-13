class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        summ = sum(nums)
        d_sum = 0

        for i in nums:
            for j in str(i):
                d_sum += int(j)

        return abs(summ - d_sum)

            