class Solution:
    def minElement(self, nums: List[int]) -> int:
        x=[]
        for i in nums:
            j=str(i)
            s=0
            for k in j:
                s+=int(k)
            x.append(s)
        return min(x)
                
                
        