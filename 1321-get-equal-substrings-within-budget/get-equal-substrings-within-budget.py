class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        res = 0
        l = 0
        curr = 0
        for i in range(len(s)):
            curr += abs(ord(s[i]) - ord(t[i]))
            while curr > maxCost:
                curr -= abs(ord(s[l]) - ord(t[l]))
                l+=1
            res = max(res, i-l+1)
            # res = curr
        return res
            
        