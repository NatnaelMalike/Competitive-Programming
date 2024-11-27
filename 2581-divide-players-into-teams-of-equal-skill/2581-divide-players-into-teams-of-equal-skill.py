class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        teams = []
        l = 0
        r = len(skill) - 1
        curr = skill[l] + skill[r]
        while(r > l):
            if curr != skill[l] + skill[r]:
                return -1
            else:
                teams.append((skill[l], skill[r]))
            l += 1
            r -= 1
        total = 0
        for x,y in teams:
            total += x*y
        return total

            