import math
import random


file = open("Names_of_ikea.txt", "r", encoding="utf-8")
words = file.read().split("\n")
words.sort(key=len)
# min_len = math.inf
# max_len = 0
min_len = len(words[0])
max_len = len(words[len(words) - 1])
bigrams = {}

for i in range(0, len(words)):
    len_word = len(words[i])

    # if len_word > max_len:
    #     max_len = len_word
    # if len_word < min_len:
    #     min_len = len_word

    if bigrams.get(words[i][0]) == None:
        bigrams[words[i][0]] = 1
    else:
        bigrams[words[i][0]] += 1

    for j in range(0, len_word - 1):
        if bigrams.get(words[i][j:j + 2]) == None:
            bigrams[words[i][j:j + 2]] = 1
        else:
            bigrams[words[i][j:j + 2]] += 1
               

list_of_bigrams = list(bigrams.items())
p = {}

for i in range(0, len(list_of_bigrams)):
    if len(list_of_bigrams[i][0]) == 1:
        if p.get("$") == None:
            p["$"] = list_of_bigrams[i][1]
        else:
            p["$"] += list_of_bigrams[i][1]      
    else:
        if p.get(list_of_bigrams[i][0][0]) == None:
            p[list_of_bigrams[i][0][0]] = list_of_bigrams[i][1]
        else:
            p[list_of_bigrams[i][0][0]] += list_of_bigrams[i][1]

keys = list(bigrams.keys())
alphabet = []

for i in range(0, len(keys)):
    if len(keys[i]) == 1:
        if alphabet.count(keys[i]) == 0:
            alphabet.append(keys[i])
        bigrams[keys[i]] /= p["$"]
    else:
        for j in range(0, 2):
            if alphabet.count(keys[i][j]) == 0:
                alphabet.append(keys[i][j])
        bigrams[keys[i]] /= p[keys[i][0]]

random_frequency = random.random()
random_len = random.randint(min_len, max_len)
keys.sort()
sum_close_to_random = 0
count = 0
my_word = ""

for i in range(0, random_len - 1):
    count = 0
    sum_close_to_random = 0
    random_frequency = random.random()
    if i == 0:
        while sum_close_to_random < random_frequency:
            if len(keys[count]) == 1:
                sum_close_to_random += bigrams[keys[count]]
                my_word = keys[count]        
            count += 1
    
    count = 0
    sum_close_to_random = 0
    random_frequency = random.random()
    while sum_close_to_random < random_frequency:
        if my_word[i] == keys[count][0] and len(keys[count]) != 1:
            sum_close_to_random += bigrams[keys[count]]
            letter = keys[count][1]
        count += 1
    
    my_word += letter
            
print(my_word, sum_close_to_random, "\n", random_frequency, random_len)