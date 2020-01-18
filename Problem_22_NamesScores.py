#Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
#containing over five-thousand first names, begin by sorting it into 
#alphabetical order. Then working out the alphabetical value for each name,
#multiply this value by its alphabetical position in the list to obtain a
##name score.
#For example, when the list is sorted into alphabetical order, COLIN, which is
#worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
#would obtain a score of 938 × 53 = 49714.
#What is the total of all the name scores in the file?
#Find the names.txt file at https://projecteuler.net/problem=22

import time

def sort_names(file):
    unsorted_names_file = open(file, "r")
    
    for name in unsorted_names_file:
        names = name.split(",")
        sorted_names = sorted(names)
        stripped_sorted = [i.replace('"', '') for i in sorted_names]
    return stripped_sorted

def get_names_score(file):
    letter_val = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8,\
        'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17,\
        'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
    name_sum = 0
    name_score = 0
    total_score = 0
    name_count = 1
    sorted_names = sort_names(file)

    for name in sorted_names:
        for char in range(len(name)):
            name_sum += letter_val[name[char]]
        name_score = name_sum * name_count
        total_score += name_score
        name_score = 0
        name_sum = 0
        name_count += 1

    return total_score

start = time.time()
total_score = get_names_score('Problem_22_namesfile.txt')
elapsed = (time.time() - start)
print("result %s returned in %s seconds." % (total_score,elapsed))