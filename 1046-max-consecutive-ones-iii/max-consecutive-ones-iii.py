class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        prefix = [0]
        for num in nums:
            if num == 0:
                x = prefix[-1] + 1  
            else:
                x = prefix[-1]     
            prefix.append(x)

        def helper(length):
            for i in range(length, len(prefix)):
                zero = prefix[i] - prefix[i - length]
                if zero <= k:
                    return True
            return False

        l =0
        r =  len(nums)
        ans = 0

        while l <= r:
            mid = (l+r) // 2
            if helper(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return ans
        


