class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0


        for right in range(len(s)):
            # count the char on right pointer
            count[s[right]] = count.get(s[right], 0) + 1

            current_max = max(count.values())
            
            # r - l + 1 is window length
            # subtract current_max gives remaining charcters
            # if remaining non-max chars is k or less, it's still valid window
            while right - left + 1 - current_max > k:
                # Subtract a count for char in left position
                count[s[left]] -= 1
                # Move pointer right
                left += 1
            
            max_freq = max(right - left + 1, max_freq)

        
        return max_freq
            

            


