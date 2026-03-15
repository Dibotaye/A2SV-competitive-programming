class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        x = max(nums)
        ans = max(nums)
        for i in range(k-1):
            x += 1
            ans += x
        return ans
        