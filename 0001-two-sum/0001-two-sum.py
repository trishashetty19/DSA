class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # value: index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
