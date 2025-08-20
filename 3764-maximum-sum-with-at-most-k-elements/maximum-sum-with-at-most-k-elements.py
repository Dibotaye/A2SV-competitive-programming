class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        max_heap = []
        for x, limit in zip(grid, limits):
            top = heapq.nlargest(limit,x)
            for i in top:
                heapq.heappush(max_heap, -i)

        summ = 0
        for _ in range(k):
            if max_heap:
                summ += -heapq.heappop(max_heap)

            
        
        return summ

       





