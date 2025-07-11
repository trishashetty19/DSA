class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr) 

        l = 0
        r = n-1

        while l<=r:
            mid = (l+r) // 2
            if arr[mid]<arr[mid+1]:
                #Peak in the right side of the mid
                l = mid + 1
            else:
                 r = mid - 1
        return l

        