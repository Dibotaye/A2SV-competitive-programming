class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res= []


        def backtrack(r, combo,i):
            if r == 0:
                res.append(list(combo))
                return
        
            for i in range(i,len(candidates)):
                curr = candidates[i]
                if curr > r:
                    continue
                combo.append(curr)
                backtrack(r-curr,combo,i)
                combo.pop()



        backtrack(target, [], 0)
        return res




        