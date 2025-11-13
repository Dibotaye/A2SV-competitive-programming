from collections import defaultdict
class TimeMap:
    

    def __init__(self):
        self.val = defaultdict(list)
        self.time = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.val[key].append(value)
        self.time[key].append(timestamp)


    def get(self, key: str, timestamp: int) -> str:
        l =0
        r = len(self.time.get(key,[])) -1
        while l<= r:
            mid = (l+r)//2
            curr = self.time[key][mid]
            if curr == timestamp:
                return self.val[key][mid]
            elif curr > timestamp:
                r = mid-1
            else:
                l = mid+1
        if r<0:
            return ""
        return self.val[key][r]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)