class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strlens = [len(string) for string in strs]
        minlen = min(strlens)

        longPre = ""
        for i in range(minlen):
            currChar = strs[0][i]
            endNow = False
            for s in strs:
                if s[i] != currChar:
                    endNow = True
            if endNow:
                return longPre
            longPre += strs[0][i]
        return longPre