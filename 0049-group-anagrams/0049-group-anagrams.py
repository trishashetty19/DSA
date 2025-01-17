class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams=defaultdict(list)
        for word in strs:
            sorted_array=''.join(sorted(word))
            anagrams[sorted_array].append(word)

        return list(anagrams.values())
        