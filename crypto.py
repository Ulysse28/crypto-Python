"""
Class Crypto
Ulysse Valdenaire
10/10/2021
"""

class Cryto():
    #constructor
    def __init__(self):
        self.listAlphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
                            "x", "y", "z"]
        
    def codeCesar(self, wordToCode, key):
        """
        wordToCode : string -> text which will be crypted
        key : int -> the gap into the alphabet list to code the message
        return : string -> the crypted message
        """

        if type(wordToCode) != str:
            return "Error, first argument must be a string"
        if type(key) != int:
            return "Error, second argument must be an integer"
        else:
            newList = []
            for i in range(len(wordToCode)):
                for j in range(len(self.listAlphabet)):
                    if wordToCode[i] == self.listAlphabet[j]:
                        for k in range(key):
                            j = j+1
                            if j >= 26:
                                j=0 
                        newList.append(self.listAlphabet[j])
            newList = "".join(newList)
        return newList


    def decodeCesar(self, wordToDecode, key):
            """
            ordToDecod : string -> text which will be decrypted
            key : int -> the gap into the alphabet list to decode the message
            return : string -> the decrypted message
            """

            if type(wordToDecode) != str:
                return "Error, first argument must be a string"
            if type(key) != int:
                return "Error, second argument must be an integer"
            else:
                newList = []
                for i in range(len(wordToDecode)):
                    for j in range(len(self.listAlphabet)):
                        if wordToDecode[i] == self.listAlphabet[j]:
                            for k in range(key):
                                j = j-1
                                if j < 0:
                                    j = 25
                            newList.append(self.listAlphabet[j])
                newList = "".join(newList)
            return newList

    def decodeCesarByForce(self, wordToDecode):
        """
        wordToDecode :string --> string you want to decode
        test every possiblities of the code ceasar
        a=b, b=c ...
        a=c, b=d...
        a=d, b=e...
        return :list --> a list of 26 strings, the 26 possibilities
        """
        newList = []
        testList=[]
        finalList = []
        for i in range(26):
            for j in range(len(wordToDecode)):
                for k in range(len(self.listAlphabet)):
                    if wordToDecode[j] == self.listAlphabet[k]:
                        for p in range(i):
                            k = k+1
                            if k >= 26:
                                k=0 
                        newList.append(self.listAlphabet[k])
            testList.append(newList)
            newList = []
        for test in testList:
            test = "".join(test)
            finalList.append(test)
 
        return finalList


crypto = Cryto()

test = "tgfbgmj bw kmak mdqkkw bw kmak vwnwdghhwmj"
print(crypto.decodeCesarByForce(test))





