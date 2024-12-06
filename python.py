import csv
import random as rand
import pandas as pd

word = input('word')
dictionary = pd.read_csv('dictionary.csv')
words = dictionary.iloc[:, 0].tolist()
temp = set() 


def test(word):
    for i in range(len(words)):
        if word == words[i]:
            return words[i]


for i in range(1000):
    word = 'snuchi'
    word_list = list(word)
    rand.shuffle(word_list)
    shuffled_word = ''.join(word_list)
    temp.add(shuffled_word)
    
    # print('?')

print(temp)


    

    




    