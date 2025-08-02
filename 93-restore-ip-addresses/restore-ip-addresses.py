class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        path = []
        def helper(s,r):
            if r == 1:
                if s and int(s) <= 255 and not (len(s)>1 and s[0] == "0"):
                    path.append(s)
                    res.append("".join(path))
                    path.pop()
                return

            for i in range(len(s)):
                val = s[:i+1]
                if int(val) > 255 or (len(val) > 1 and val[0] == "0"):
                    return 
                
                path.append(val)
                path.append(".")
                helper(s[i+1:], r-1)
                path.pop()
                path.pop()
        helper(s,4)
        return res
            
        