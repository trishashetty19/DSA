class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 1
        for i in range(2, len(nums)):
           if nums[i]!=nums[start-1]:
             start+=1
             nums[start] = nums[i]
        return start+1

    



        