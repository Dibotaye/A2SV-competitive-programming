class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(path, open, close):
            if close == n and open == n:
                res.append(path)
                return
            
            if open < n: 
                backtrack(path +"(", open+1,close)
                
            if close < open:
                backtrack(path+")", open, close+1)


                
        backtrack("",0,0)
        return res




                