class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
            
        max_rep = 0
        n = len(s)

        # Try every unique character present in the string as the target character
        for ch in set(s):
            i = 0
            j = 0
            count = 0
            
            while j < n:
                # If the current character matches our target, expand the window
                if s[j] == ch:
                    j += 1
                # If it doesn't match, we use one of our 'k' replacements
                elif count < k:
                    count += 1
                    j += 1
                # If we've run out of replacements, shrink the window from the left
                else:
                    if s[i] != ch:
                        count -= 1
                    i += 1
                
                max_rep = max(max_rep, j - i)

        return max_rep