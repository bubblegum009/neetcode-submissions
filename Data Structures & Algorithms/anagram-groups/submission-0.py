class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map=defaultdict(list)
        for s in strs:
            k="".join(sorted(s))
            anagram_map[k].append(s)

        return list(anagram_map.values())