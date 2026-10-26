class Solution:
    def minWindow(self, s: str, t: str) -> str:
        td = {}
        for letter in t:
            td[letter] = td.get(letter, 0) + 1
        # print(td)
        
        l = 0
        r = 0
        best = len(s) + 10
        bestIndex = -1
        wd = {}

        while r < len(s):
            # print(l, r, s[l:r+1])
            wd[s[r]] = wd.get(s[r], 0) + 1
            while self.dind(td, wd):
                # print("inner", s[l: r+1])
                if r - l + 1 < best:
                    best = r - l + 1
                    bestIndex = l
                wd[s[l]] -= 1
                l += 1
            r += 1
        
        # print(bestIndex, bestIndex + best)

        if bestIndex == -1:
            return ""
        else:
            return s[bestIndex: bestIndex + best]

            


    def dind(self, td, wd):
        for letter in td:
            if letter in wd and wd[letter] >= td[letter]:
                pass
            else:
                return False
        return True
