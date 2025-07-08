class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)

        for i in range(0,n):
            isSwap = False
            for j in range(n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    isSwap = True
            if not isSwap:
                break

        return nums

        