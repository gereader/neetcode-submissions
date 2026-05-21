class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        current_total = numbers[left] + numbers[right]

        while current_total != target:

            # Shift Right pointer to lower numbers
            if current_total > target:
                right -= 1
            
            # Shift Left pointer to higher numbers
            if current_total < target:
                left += 1
            
            current_total = numbers[left] + numbers[right]


        # Always 1 solution, and it's 1-indexed so add 1
        return [left + 1, right + 1]
            
