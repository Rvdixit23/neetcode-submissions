class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            for char in s:
                result += char
            result += "`"
        return result

    def decode(self, s: str) -> List[str]:
        ans = []
        res = ""
        for char in s:
            if char != "`":
                res += char
            else:
                ans.append(res)
                res = ""
        return ans