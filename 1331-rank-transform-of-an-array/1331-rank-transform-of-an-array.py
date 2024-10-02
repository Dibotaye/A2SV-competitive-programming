class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        num=sorted(set(arr))
        x={}
        for i in range(len(num)):
            x[num[i]]=i+1
        y=[]
        for i in arr:
            y.append(x[i])
        return y
            
        