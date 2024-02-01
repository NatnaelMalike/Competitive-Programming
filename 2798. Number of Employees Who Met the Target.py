class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for hr in range(len(hours)):
            if(hours[hr] >= target):
                count += 1
        return count
        