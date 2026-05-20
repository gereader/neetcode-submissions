class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for item in nums:
            if item in seen:
                return True
            else:
                # Count
                seen[item] = seen.get(item, 0) + 1
        return False