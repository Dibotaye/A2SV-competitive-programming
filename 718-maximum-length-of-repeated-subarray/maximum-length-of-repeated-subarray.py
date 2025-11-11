class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def helper(mid):
            hash1 = set()
            hash2 = set()
            base = 101
            mod = 2**32
            a = pow(base, mid, mod)
            currhash = 0
            for i in range(n):
                currhash = currhash *base + nums1[i]
                if i >= mid:
                    currhash -= nums1[i-mid]* a
                currhash %= mod

                if i >= mid-1:
                    hash1.add(currhash)
            currhash = 0
            for i in range(m):
                currhash = currhash *base + nums2[i]
                if i >= mid:
                    currhash -= nums2[i-mid] * a
                currhash %= mod

                if i >= mid -1:
                    hash2.add(currhash)
            return len(hash1.intersection(hash2)) >0


        

        n= len(nums1)
        m = len(nums2)
        l =0
        r = min(n,m)
        while l< r:
            mid= (r+l+1)//2
            if helper(mid):
                l = mid
            else:
                    r = mid-1
               
        return l






            
        