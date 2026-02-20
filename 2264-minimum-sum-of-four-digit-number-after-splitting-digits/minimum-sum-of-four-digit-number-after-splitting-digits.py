class Solution:
    def minimumSum(self, num: int) -> int:
        nums = sorted(str(num))
        x = int(nums[0] + nums[2])
        y = int(nums[1] + nums[3])
        return x + y



        