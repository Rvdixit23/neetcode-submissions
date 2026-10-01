class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = 0
        p2 = 0
        answer = []
        while p1 < len(word1) and p2 < len(word2):
            answer.append(word1[p1])
            answer.append(word2[p2])
            p1 += 1
            p2 += 1
        if p1 == len(word1):
            leftover = word2
            p = p2
        elif p2 == len(word2):
            leftover = word1
            p = p1
        while p < len(leftover):
            answer.append(leftover[p])
            p += 1
        return "".join(answer)

        