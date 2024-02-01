class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = ""
        w2 = ""
        mergedString = ""
        smallestStr = 0
        if(len(word1) > len(word2)):
            w1  = word1[slice(len(word2), len(word1))]
            smallestStr = len(word2)
        else:
            w2  = word2[slice(len(word1), len(word2))]
            smallestStr = len(word1)
        for char in range(smallestStr*2):
            if(char%2 == 0):
                mergedString += word1[ceil(char/2)]
            else:
                mergedString += word2[floor(char/2)]
        if(smallestStr == len(word1)):
            mergedString += w2
        else:
            mergedString += w1
        return mergedString

        