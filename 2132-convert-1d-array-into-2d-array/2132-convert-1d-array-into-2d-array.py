import numpy as np
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        if len(original)!=m*n:
            return[]
        my_array=np.array(original)
        res=my_array.reshape(m,n)
        return res
        