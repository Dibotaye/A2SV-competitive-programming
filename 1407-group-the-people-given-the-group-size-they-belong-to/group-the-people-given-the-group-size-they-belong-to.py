class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list) 
        res = []

        for i,j in enumerate(groupSizes):
            groups[j].append(i)
            if len(groups[j]) == j:
                res.append(groups[j])
                groups[j] = []  

        return res
            

