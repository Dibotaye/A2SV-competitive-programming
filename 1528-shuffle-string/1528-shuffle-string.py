class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res=[None]*len(s)
        for i in range(len(indices)):
            res[indices[i]]=s[i]
        return "".join(res)