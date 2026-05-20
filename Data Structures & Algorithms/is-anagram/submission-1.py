class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # make sure str same size
        if len(s) != len(t):
            return False

        # Solve by counter
        counter_s = {}
        counter_t = {}

        for i in range(len(s)):
            # Count number of times char shows for each
            counter_s[s[i]] = counter_s.get(s[i], 0) + 1
            counter_t[t[i]] = counter_t.get(t[i], 0) + 1
        
        # If they come out same counts, then they are anagram
        return counter_s == counter_t