class Solution:
    def firstUniqChar(self, s: str) -> int:
        x={}
        for i in s:
            if i not in x:
                x[i]=1
            else:
                x[i]+=1
        for i in range(len(s)):
            if x[s[i]]==1:
                return i
        return -1
        