class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n=sorted(arr)
        mindif=n[1]-n[0]
        for i in range(len(n)-1):
            if mindif > n[i+1]-n[i]:
                mindif = n[i+1]-n[i]
        x=[]
        for i in range(len(n)-1):
            if mindif == n[i+1]-n[i]:
                x.append([n[i],n[i+1]])
        return x
                
            
        