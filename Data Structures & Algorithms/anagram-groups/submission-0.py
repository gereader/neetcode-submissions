class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = {}

        for i, w in enumerate(strs):
            sorted_word = ''.join(sorted(list(w)))
            if sorted_word in seen:
                seen[sorted_word].append(strs[i])
            else:
                seen[sorted_word] = [strs[i]]

        return [value for value in seen.values()] 
