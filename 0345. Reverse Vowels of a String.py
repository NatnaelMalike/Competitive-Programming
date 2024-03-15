class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        wordList = list(s)
        beg = 0
        end = len(s)-1
        while(beg < end):
            if wordList[beg] in vowels and wordList[end] in vowels:
                wordList[beg], wordList[end] = wordList[end], wordList[beg]
                beg += 1
                end -= 1
            elif wordList[beg] in vowels:
                end -= 1
            else:
                beg += 1
        return "".join(wordList)
