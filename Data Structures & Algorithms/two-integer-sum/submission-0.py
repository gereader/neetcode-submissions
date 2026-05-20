class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for i, num in enumerate(nums):
            # Leaving this commented line as a reminder, I couldn't figure out why this wasn't working, index 0 was returnign but 0 is false so i couldn't rely on "none"
            # if hashmap.get(target - num):
            if target - num in hashmap:
                return [hashmap[target - num], i]

            hashmap[num] = i    
