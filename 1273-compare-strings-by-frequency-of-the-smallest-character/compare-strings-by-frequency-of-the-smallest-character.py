class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        f = []
        for i in words:
            c = Counter(i)
            f.append(c[min(i)])

        f.sort()

        n = len(f)
        res = []
        for i in queries:
            c = Counter(i)
            f_query = c[min(i)]
            count = 0
            for i in range(n):
                if f[i] > f_query:
                    count = n-i
                    break

            res.append(count)
        return res




