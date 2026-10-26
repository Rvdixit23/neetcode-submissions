class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k >= len(arr):
            return arr
        
        ans = []
        bd = abs(x - arr[0])
        bi = 0
        for index, ele in enumerate(arr):
            if abs(x - ele) < bd:
                bi = index
                bd = abs(x - ele)

        l = bi
        r = bi

        # print(l, r)
        #        2  3  4
        # [3, 4, 5, 6, 7, 9]

        while r - l + 1 < k:
            print(l, r)
            if l == 0:
                r += 1
            elif r == len(arr) - 1:
                l -= 1
            else:
                if abs(arr[l - 1] - x) > abs(arr[r + 1] - x):
                    r += 1
                else:
                    l -= 1
        return arr[l:r+1]



    