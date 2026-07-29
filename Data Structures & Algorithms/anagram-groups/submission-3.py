class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        fic = {}

        for i in strs:
            key = "".join(sorted(i))
            if key in fic:
                fic[key].append(i)
            else:
                fic[key] = [i]
        
        return list(fic.values())