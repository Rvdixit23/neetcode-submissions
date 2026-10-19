class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        chars = set()
        chars.add(s[0])
        maxLen = 1
    
        L, R = 0, 1
# bcada
# 
        while R < len(s):
            # print("Looking at index", R , "and found", s[R])
            if s[R] not in chars:
                chars.add(s[R])
                maxLen = max(maxLen, len(chars))
                # print("Added", s[R])
                # print("Chars is", chars)
            else:
                maxLen = max(maxLen, len(chars))
                # print("Moving L")
                while s[R] in chars:
                    # print("Removing", s[L], "from chars")

                    chars.remove(s[L])
                    # print("Chars is", chars)
                    L += 1
                chars.add(s[R])
                L + 1
            
            R += 1
    
        return maxLen
