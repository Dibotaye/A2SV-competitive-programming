class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[(0, 0)] for _ in range(length)]
        self.id = 0

    def set(self, index: int, val: int) -> None:
        if self.arr[index][-1][0] == self.id:
            self.arr[index][-1] = (self.id,val)
        else:
            self.arr[index].append((self.id,val))


    def snap(self) -> int:
        snap_id = self.id
        self.id += 1
        return snap_id
        

    def get(self, index: int, snap_id: int) -> int:
        res = self.arr[index]
        l= 0
        r = len(res) - 1

        while l <= r:
            mid = (l + r) // 2
            if res[mid][0] <= snap_id:
                l = mid + 1
            else:
                r = mid - 1

        return res[r][1]






# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)