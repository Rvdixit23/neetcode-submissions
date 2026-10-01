class Solution:
    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        isDeleted = False

        while start < end:
            if s[start] != s[end]:
                # If is deleted then doomed
                if isDeleted:
                    return False
                # Check if char can be deleted to fix it
                else:
                    answer = False
                    if s[start + 1] == s[end]:
                        answer = self.isPalindrom(s, start + 1, end)
                    if s[start] == s[end - 1]:
                        answer = answer or self.isPalindrom(s, start, end - 1)
                    return answer
            start += 1
            end -= 1
        return True

    def isPalindrom(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
                