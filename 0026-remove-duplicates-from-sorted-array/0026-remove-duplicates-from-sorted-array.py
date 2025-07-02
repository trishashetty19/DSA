class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 0
        for i in range(1, len(nums)):
           if nums[i]!=nums[i-1]:
             start+=1
             nums[start] = nums[i]
        return start+1

    



        