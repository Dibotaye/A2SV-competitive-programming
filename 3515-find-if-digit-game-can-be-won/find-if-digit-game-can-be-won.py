class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        x = 0
        y = 0
        z = 0
        for i in nums:
            if 1 <= i <= 9:
                x += i
            elif 10 <= i <= 99:
                y += i
            else:
                z += i

        return (x > y+z or y > x + z)

            