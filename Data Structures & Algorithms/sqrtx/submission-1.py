class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x

        m = (l + r) // 2
        while l <= r:
            m = (l + r) // 2
            if m ** 2 == x:
                return m
            elif m ** 2 < x:
                l = m + 1
            elif m ** 2 > x:
                r = m - 1
        # print(m)
        return m - 1 if m ** 2 > x else m
        
