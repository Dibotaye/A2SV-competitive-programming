class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        for i in operations:
            if i == "+":
                arr.append(arr[-1] + arr[-2])
            elif i == "D":
                arr.append(2 *arr[-1])
            elif i == "C":
                arr.pop()
            else:
                arr.append(int(i))

        return sum(arr)


        