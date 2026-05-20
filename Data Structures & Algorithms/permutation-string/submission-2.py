class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, len(s1) - 1

        # Sort once to save some time
        s1 = sorted(s1)
        while right < len(s2):
            if sorted(s2[left:right + 1]) == s1:
                return True
            # Shift window right
            right += 1
            left += 1
        return False

    # 50ms version
    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     left, right = 0, len(s1) - 1
    #     while right < len(s2):
    #         if sorted(s2[left:right + 1]) == sorted(s1):
    #             return True
    #         # Shift window right
    #         right += 1
    #         left += 1
    #     return False