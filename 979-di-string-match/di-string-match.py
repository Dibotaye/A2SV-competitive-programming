class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        l = 0
        r =  n
        res = []
        for i in s:
            if i == 'I':
                res.append(l)
                l += 1
            else: 
                res.append(r)
                r -= 1

        res.append(l)
        return res
            