class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        for ele in items:
            if ruleKey == 'type':
                if ele[0] == ruleValue:
                    count += 1
            if ruleKey == 'color':
                if ele[1] == ruleValue:
                    count += 1
            if ruleKey == 'name':
                if ele[2] == ruleValue:
                    count += 1
        return count