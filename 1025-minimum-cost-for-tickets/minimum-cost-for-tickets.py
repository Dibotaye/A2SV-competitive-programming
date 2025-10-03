class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0]* (days[-1]+1)

        for i in range(len(dp)):
            if i not in days:
                dp[i] = dp[i-1]
                
            else:
                cost1 = dp[i-1] + costs[0]
                if i-7 < 0:
                    cost7 = dp[0] + costs[1]
                else:
                    cost7 = dp[i-7] +costs[1]
                if i-30 < 0:
                    cost30 = dp[0] + costs[2]
                else:
                    cost30 = dp[i-30] +costs[2]


                dp[i] = min(cost1,cost7,cost30)


        return dp[-1]
                
                

