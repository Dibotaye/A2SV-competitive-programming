class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        count = sorted(freq.values())
        count.reverse()

        ans = 0
        for i, j in enumerate(count):
            c = (i//8)+1
            ans += j* c
        
        return ans

