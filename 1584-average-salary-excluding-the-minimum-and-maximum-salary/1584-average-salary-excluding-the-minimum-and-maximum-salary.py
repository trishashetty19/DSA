class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        total_sum=sum(salary[1:-1]) #Excluding minimum and maximum element
        total_avg=total_sum/(len(salary)-2) #Dividing it with len(salary)-2 elements
        return total_avg