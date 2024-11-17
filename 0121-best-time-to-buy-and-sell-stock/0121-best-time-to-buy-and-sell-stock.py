class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minprof= float("inf")
        maxprof= 0
        for i in prices:
            if i<minprof:
                minprof=i
            profit= i-minprof
            if profit > maxprof:
                maxprof=profit
        return maxprof
                
            
        