class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output  = []
        output.append(nums[0])

        for i in range(1,n):
            sum = output[i-1] + nums[i]
            output.append(sum)
        
        return output
        