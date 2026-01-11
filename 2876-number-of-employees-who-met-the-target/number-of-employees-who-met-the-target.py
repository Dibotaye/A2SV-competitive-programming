class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        summ = 0 
        for i in hours:
            if i >= target:
                summ += 1
        return summ