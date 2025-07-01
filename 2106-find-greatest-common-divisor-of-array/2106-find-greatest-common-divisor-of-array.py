class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = min(nums)
        b = max(nums)
        return self.gcd(a,b)

    def gcd(self, a: int, b: int) -> int:
        if b==0:
            return a 
        return self.gcd(b, a%b)

        



        