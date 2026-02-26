class Solution:
    def maximum69Number (self, num: int) -> int:
        n = str(num)
        ans = ""
        for i in range(len(n)):
            print(ans)  
            if n[i] == "6":
                ans += "9"
                ans += n[i+1:]
                
                break    
            else:
                ans += n[i]
                # print(ans
             
        return int(ans)