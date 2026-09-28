class Solution:
    def decodeString(self, s: str) -> str:
        index = 0
        answer, _ = self.rec(s, index)
        return answer

    def rec(self, s, index):
        answer = ""
        while index < len(s) and s[index] != "]":
            if s[index].isalpha():
                answer += s[index]
            elif s[index].isdigit():
                num = ""
                while s[index].isdigit():
                    num += s[index]
                    index += 1
                index -= 1
                num = int(num)
            elif s[index] == "[":
                innerAns, index = self.rec(s, index + 1)
                answer += num * innerAns
            index += 1
        return answer, index