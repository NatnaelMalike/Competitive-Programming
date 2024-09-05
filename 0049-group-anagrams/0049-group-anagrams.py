class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {} 
        for word in strs:
            so ="".join(sorted(word)) 
            if so not in dict:
                dict[so] = [word] 
            else:
                dict[so].append(word)
        return dict.values()
        

        