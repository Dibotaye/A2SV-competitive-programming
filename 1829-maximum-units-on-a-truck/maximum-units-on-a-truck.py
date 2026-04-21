class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1],reverse=True)
        ans = 0
        remain = truckSize
        for i,j in boxTypes:
            boxes_to_take = min(remain,i)
            ans += boxes_to_take * j
            remain -= boxes_to_take


        return ans

        