class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Point at start/end of list
        left = 0
        right = len(nums) - 1

        while left <= right:
            # Find middle
            middle = (left + right) // 2

            if nums[middle] == target:
                # Found it
                return middle
            elif nums[middle] < target:
                # We know it's right of middle
                left = middle + 1
            else:
                # We know it's left of middle
                right = middle - 1
        
        return -1