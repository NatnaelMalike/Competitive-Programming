class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t'
                    ,'u','v','w','x','y','z']
        keyTable = {}
        newKey = (key.replace(" ", ""))
        messArr = [x for x in message]
        lt = 0
        for i in range(len(newKey)):
            if newKey[i] not in keyTable:
                keyTable[newKey[i]] = alphabets[lt]
                lt += 1
        for i in range(len(messArr)):
            if messArr[i] != ' ':
                messArr[i] = keyTable[messArr[i]]
        return "".join(messArr)

        




        