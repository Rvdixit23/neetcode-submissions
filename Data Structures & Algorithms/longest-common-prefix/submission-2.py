class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smolStr = min(strs, key=len)
        minlen = len(smolStr)

        prefixStr = ""
        for i in range(minlen):
            currChar = smolStr[i]
            for s in strs:
                if s[i] != currChar:
                    return prefixStr
            prefixStr += currChar
        return prefixStr