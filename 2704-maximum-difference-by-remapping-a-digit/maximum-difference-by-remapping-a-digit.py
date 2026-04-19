class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        max_s = s
        for i in s:
            if i != "9":
                max_s = s.replace(i,"9")
                break
        
      
        min_s = s
        for i in s:
            if i != "0":
                min_s = s.replace(i,"0")
                break
        
        ans = int(max_s) - int(min_s)
        return ans
            
