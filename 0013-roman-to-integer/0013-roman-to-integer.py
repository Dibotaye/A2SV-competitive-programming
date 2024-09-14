class Solution:
    def romanToInt(self, s: str) -> int:
        des = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        total=0
        for i in range(len(s)):
            if i+1<len(s) and des[s[i]]<des[s[i+1]]:
                total-=des[s[i]]
            else:
                total+=des[s[i]]
        return total       
        