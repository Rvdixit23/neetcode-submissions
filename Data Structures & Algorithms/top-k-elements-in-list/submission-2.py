class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fkd = {}
        fkd[0] = set(nums)
        
        nkd = {}
        
        for num in nums:
            nkd[num] = nkd.get(num, 0) + 1
            if nkd[num] not in fkd:
                fkd[nkd[num]] = set()
            fkd[nkd[num]].add(num)
            fkd[nkd[num] - 1].remove(num)
        
        answer = []
        print(fkd)
        for freq in range(len(nums), -1, -1):
            if len(answer) < k and freq in fkd:
                answer.extend(fkd[freq])

        return answer

        
        # freq = {}
        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1
        # print(freq)
        # keys = list(freq.keys())
        # keys.sort(key=lambda x: freq[x], reverse=True)
        # return keys[0:k]