class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slen = len(s)
        tlen = len(t)

        if slen != tlen:
            return False

        tdict = {}
        sdict = {}
        for index in range(slen):
            schar = s[index]
            tchar = t[index]
            if schar in sdict:
                sdict[schar] += 1
            else:
                sdict[schar] = 1
            if tchar in tdict:
                tdict[tchar] += 1
            else:
                tdict[tchar] = 1
            
        for letter in tdict:
            if tdict.get(letter, -1) != sdict.get(letter, -1):
                return False

        return True