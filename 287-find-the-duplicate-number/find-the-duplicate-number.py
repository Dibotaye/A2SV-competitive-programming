class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        c = defaultdict(int)
        for i in nums:
            c[i] += 1

        for i in nums:
            if c[i] > 1:
                return i

        