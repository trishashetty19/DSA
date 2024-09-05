class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res=nums1+nums2
        res.sort()
        length =len(res)

        if length%2==1:
            return res[length//2]
        else:
            mid1=res[length//2]
            mid2=res[length//2-1]
            return (mid1+mid2)/2

        