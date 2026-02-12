class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        c = defaultdict(int)
        for i in s:
            c[i] += 1
        print(c)
        odd = False
        for i in c:
            if c[i] % 2 == 0:
                ans += c[i]
            else:
                ans += c[i] - 1
                odd = True
        if odd:
            ans += 1
        return ans

        
        