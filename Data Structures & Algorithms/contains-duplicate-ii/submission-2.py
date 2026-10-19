class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        front = 0
        back = 1

        eles = { nums[front] : 1 }
        while back < k:
            if nums[back] in eles:
                return True
            eles[nums[back]] = 1
            back += 1

        while back < len(nums):
            if nums[back] in eles:
                return True
            eles[nums[back]] = 1
            eles.pop(nums[front])
            front += 1
            back += 1
        
        return False
            

