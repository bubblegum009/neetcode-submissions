class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams=defaultdict(list)
        for i in range(0,len(strs)):
            ch=tuple(sorted(strs[i]))
            
            anagrams[ch].append(strs[i])
        return [i for i in anagrams.values()]
