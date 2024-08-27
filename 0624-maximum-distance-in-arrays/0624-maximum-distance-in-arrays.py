class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        n=len(arrays)
        min_value=min(arrays[0])
        max_value=max(arrays[0])

        max_dis=0
        for i in range(1,n):
            curr_max=max(arrays[i])
            curr_min=min(arrays[i])
            max_dis=max(max_dis,max(abs(curr_max-min_value),abs(max_value-curr_min)))
            min_value=min(min_value,curr_min)
            max_value=max(max_value,curr_max)

        return max_dis