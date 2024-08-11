class Solution:
    def countSeniors(self, details: List[str]) -> int:
        older = 0
        for person in details:
            if int(person[11:13]) > 60:
                older += 1
        return older
        