class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        curr=1
        i=0
        while (1):
            if curr not in arr:
                i+=1
                if i==k:
                    return curr
            curr+=1
            
            
        