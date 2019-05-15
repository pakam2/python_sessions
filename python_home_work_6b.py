from shutil
from collections import Counter

import copyfile
import random
import os

#1
def write_list_to_file(path_to_file, ex_list):
    with open(path_to_file, "w") as my_file:
        for numb in ex_list:
            my_file.write("%d\n" % numb)

write_list_to_file('test.txt', [1, 2, 3, 4])

#2
def copy_con_to_another_file(path1, path2):
    copyfile(path1, path2)

copy_con_to_another_file('one.txt', 'two.text')

#3
def combine_lines(path1, path2):
    with open(path1) as f1, open(path2) as f2:
        for line1, line2 in zip(f1, f2):
            print(line1 + line2)

combine_lines('one.txt','two.txt')

#4
def write_random_line(path1):
    l = open(path1).read().splitlines()
    print(random.choice(l))

write_random_line('one.txt')

#5
file1 = open('one.txt')
print(file1.read())

#6
def read_first_line(path):
    with open(path) as f1:
        for line in f1:
            print(line)
            break

read_first_line('one.txt')

#7
def append_and_read(path, text):
    with open(path, "w") as f1:
        f1.write(text)
    read_text = open(path)
    print(read_text.read())

append_and_read('one.txt',"asdasda")


#8
def read_last_n_lines(path, number_of_lines):
    all_lines = []
    with open(path,'r') as f1:
        for line in f1:
            all_lines.append(line)
    length = len(all_lines) - 1
    counter = 0
    while number_of_lines > 0:
        print(all_lines[length - counter])
        counter += 1
        number_of_lines -= 1

read_last_n_lines('one.txt', 5)

#9
def store_in_list(path):
    all_lines = ''
    with open(path, 'r') as f1:
        all_lines = f1.readlines()
    retrun all_lines

#10
def store_in_variable(path):
    all_lines = ''
    with open (path, "r") as f1:
        all_lines = f.readlines()
    return all_lines

store_in_variable('one.txt')

#11
def store_in_array(path):
    m_array = []
    with open(path) as f1:
        for line in f1:
            m_array.append(line)
    return m_array

store_in_array('one.txt')

#12
def longest_word(path):
    with open(path, 'r') as f1:
        words = f1.read().split()
    max_of_word = len(max(words, key=len))
    for word in words:
        if len(word) == max_of_word:
            return word

longest_word('one.txt')

#13
def count_lines(path):
    counter = 0
    with open(path) as f1:
        for line in f1:
            counter +=1
    return counter

combine_lines('one.txt')

#14
def count_words_in_file(path):
    with open(path) as f1:
        return Counter(f1.read().split())

print(count_words_in_file("one.txt"))


#15
os.stat('one.txt').st_size
#16
print(open('one.txt', 'r').closed)

#17
def remove_newlines(path):
    lines = open(path).readlines()
    res = []
    for l in lines:
        res.append(l.rstrip('\n'))
    return res

print(remove_newlines("one.txt"))
