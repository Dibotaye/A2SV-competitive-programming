class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        n = len(times)
        self.res= [-1]*n
        self.times = times
        self.d = defaultdict(int)
        curr =None

        for i in range(n):
            self.d[persons[i]] += 1
            if curr is None or self.d[persons[i]] >= self.d[curr]:
                curr = persons[i]
            self.res[i] = curr

        

    def q(self, t: int) -> int:
        return self.res[bisect_right(self.times, t)-1]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)