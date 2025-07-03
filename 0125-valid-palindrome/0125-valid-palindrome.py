class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ''.join(i.lower() for i in s if i.isalnum())
        return ans == ans[::-1]
        
        