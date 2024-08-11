class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return []
        nums.sort()
        duplicates=[]
        for i in range(0,len(nums)):
            if nums[i]==nums[i-1] and (not duplicates or nums[i] != duplicates[-1]):
                duplicates.append(nums[i])
        return duplicates