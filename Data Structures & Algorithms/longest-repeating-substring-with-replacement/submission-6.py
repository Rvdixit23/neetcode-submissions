class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if k >= len(s) - 1:
            return len(s)
        
        best = max(k, 1)
        L, R = 0, 0
        freq = {}

        # while R < k:
        #     freq[s[R]] = freq.get(s[R], 0) + 1
        #     print(freq)
        #     R += 1

        
        while R < len(s):
            freq[s[R]] = freq.get(s[R], 0) + 1
            # print(freq)
            mfe = max(freq, key=lambda x:freq[x])
            # print(L, R, mfe)
            if R - L + 1 > freq[mfe] + k:
                freq[s[L]] -= 1
                L += 1
            best = max(best, R - L + 1)
            R += 1
        return best
        


        # Move R until k and build up dict
        # Keep moving R as long as there is a possibility of a new best
        # Possibility of new best is when 
            # Most frequent element is coming up
            # Check for new best in every loop

