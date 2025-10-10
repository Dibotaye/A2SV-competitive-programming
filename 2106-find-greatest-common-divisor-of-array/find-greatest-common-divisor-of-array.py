class Solution:
    def findGCD(self, nums: List[int]) -> int:
        gcd = 1    
        smaller = min(nums)
        larger = max(nums)
        for i in range(1,smaller+1):
            if smaller % i == 0 and larger % i == 0:
                gcd = i
        
        return gcd



        