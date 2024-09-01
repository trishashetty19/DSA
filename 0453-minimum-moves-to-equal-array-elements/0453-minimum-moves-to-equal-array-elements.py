class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_element=min(nums)
        moves=0
        for num in nums:
            moves+=(num-min_element)
        return moves
        