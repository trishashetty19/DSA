class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()[::-1]
        joined_word = ' '.join(word)
        return joined_word
        