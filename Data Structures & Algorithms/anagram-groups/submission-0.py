class Solution:
    def stot(self, s):
        arr = [0 for i in range(26)]
        for letter in s:
            arr[(ord(letter) - ord('a'))] += 1
        return tuple(arr)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anDict = {}
        for index, s in enumerate(strs):
            stup = self.stot(s)
            if stup in anDict:
                anDict[stup].append(strs[index])
            else:
                anDict[stup] = [strs[index]]
        
        finalAns = []
        for key in anDict:
            finalAns.append(anDict[key])
        return finalAns