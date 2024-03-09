#!/usr/bin/env python3

def return_evens(num_list):
    even = []
    # for i in range(len(num_list)):
    for i in num_list:
        if i % 2 == 0:
            even.append(i)

    return even

        


def make_exclamation(sentence_list):
    new_sentence = [''.join([element, '!']) for element in sentence_list]  
    return new_sentence
    # for value in sentence_list:
    #     new_sentence.append(str(value))
    
    # print (new_sentence)
    





# lib/app.py
# print("Hello world!", end=" ")
# print("Hello sun!", end="!! ")
# print("Hello sky!", end="!!!\n")