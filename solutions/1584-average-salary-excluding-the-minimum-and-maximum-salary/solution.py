class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary.pop()
        salary.pop(0)
        s=sum(salary)
        return s/len(salary)
