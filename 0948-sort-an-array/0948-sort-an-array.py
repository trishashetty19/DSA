class Solution:
    def merge(slef, nums, l, mid, r):
        a = []
        b = []

        for i in range(l,mid+1):
            a.append(nums[i])
        for j in range(mid+1, r+1):
            b.append(nums[j])

        i,j,k = 0,0,l
        
        while k<=r:
            if j==len(b):
                nums[k] = a[i]
                i+=1
                k+=1
            elif i==len(a):
                nums[k]= b[j]
                j+=1
                k+=1
            elif a[i]<b[j]:
                nums[k] = a[i]
                i+=1
                k+=1
            else:
                nums[k]= b[j]
                j+=1
                k+=1
            

    def mergeSort(self, nums, l , r):
        #Base case
        if l>=r:
            return

        #Recursive case 
        mid=(l+r)//2
        self.mergeSort(nums,l,mid)
        self.mergeSort(nums,mid+1,r)

        self.merge(nums, l, mid, r)
        
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums,0,len(nums)-1)
        return nums
        