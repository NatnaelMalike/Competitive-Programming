class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = 0
        r = len(skill) - 1
        curr = skill[l] + skill[r]
        tot = 0
        while(r > l):
            if curr != skill[l] + skill[r]:
                return -1
            tot += skill[l] * skill[r]
            l += 1
            r -= 1
        return tot

            