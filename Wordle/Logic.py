import random

class Logic :
    def remove_trash(self, list, target):
        for item in list[::] :
            if item == target:
                list.remove(item)

        return list

    def check(self,word):

        out = ''
        print(self.RANDOM == '')
        print(self.RANDOM == '\n')
        print(self.RANDOM)
        word = word.lower()
        for i in range(len(word)):
            print(i)
            print(word[i] + self.RANDOM[i])
            if word[i] == self.RANDOM[i]:
                out += 'x'
            elif word[i] in self.RANDOM:
                out += 'l'
            else:
                out += 'o'
        return out

    def __init__(self):
        self.RANDOM = ''
        with open('words5.txt','r') as reader:
            list_words = self.remove_trash(reader.readlines(), "\n")
            self.RANDOM = random.choice(list_words)









#x -> position correct letter correct
#l -> letter correct
#o -> letter not in word



