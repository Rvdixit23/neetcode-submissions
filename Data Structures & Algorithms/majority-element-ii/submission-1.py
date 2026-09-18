class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Dict
        # Maintain freq
        # Traverse Dict
        # Append element with freq > n/3
        # O(n) space and O(n) time

        # 5, 5, 3, 1, 5, 5, 2, 2, 2, 2, 
        # x, y

        # Need O(1) space and O(n) time
        # No Dict, no set
        # Iterate through elements (Must do)
        # [5,5,3,5||||,2,2,2||||,2,2,5]
        # Split array into 3 pieces
        # Element HAS to be present in more than 1 piece

        # There can be only 0, 1 or 2 elements at most which have it
        # Hashamp with only 2 keys
        #4, 4, 4, 4, 3, 3, 3, 2, 2, 2


        n1 = None
        n2 = None
        c1 = 0
        c2 = 0

        for num in nums:
            if num == n1:
                c1 += 1
            elif num == n2:
                c2 += 1
            elif c1 == 0:
                n1 = num
                c1 = 1
            elif c2 == 0:
                n2 = num
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
            
        c1 = 0
        c2 = 0
        for num in nums:
            if num == n1:
                c1 += 1
            if num == n2:
                c2 += 1
        
        answer = []
        if c1 > len(nums) // 3:
            answer.append(n1)
        if c2 > len(nums) // 3:
            answer.append(n2)
        return answer

        
        
        
        
        
        
        
        # O(n) time and O(n) space
        # freq = {}
        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1
        # answer = []
        # for num in freq:
        #     if freq[num] > len(nums) // 3:
        #         answer.append(num)
        # return answer