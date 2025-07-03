class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.split()[::-1]
        ans = word[0]
        return len(ans)
        