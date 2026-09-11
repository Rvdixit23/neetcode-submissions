class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            for char in s:
                result += char
            result += "ಳ"
        return result

    def decode(self, s: str) -> List[str]:
        ans = []
        res = ""
        for char in s:
            if char != "ಳ":
                res += char
            else:
                ans.append(res)
                res = ""
        return ans