"""Example docstring"""

import itertools
from collections import Counter
#LIST
#1
def are_dicts_empty(list_of_dicts):
    """Function"""
    for n in list_of_dicts:
        if not n == {}:
            return False
    return True

# faster solution
def is_list_w_empty_dicts(l_dicts):
    """Function"""
    for d in l_dicts:
        if d:
            return False
    return True

print(are_dicts_empty([{}, {}, {}]))
print(are_dicts_empty([{1, 2}, {}, {}]))

#2
def remove_duplicates(n_list):
    """Function"""
    new_list =[]
    for x in n_list:
        if x not in new_list:
            new_list.append(x)
    return new_list

def rem_redundant_el_from_list1(l_of_lists):
    """Function"""
    return [list(t) for t in set(tuple(l) for l in l_of_lists)]


def rem_redundant_el_from_list2(l_of_lists):
    """Function"""
    return [l for n, l in enumerate(l_of_lists) if l not in l_of_lists[:n]]


def rem_redundant_el_from_list3(l_of_lists):
    """Function"""
    filtered_l_of_lists = []
    for l in l_of_lists:
        if l not in filtered_l_of_lists:
            filtered_l_of_lists.append(l)
    return filtered_l_of_lists


print(remove_duplicates([[10,20], [40], [30, 56, 25], [10,20], [33], [40]]))

LIST_OF_LISTS = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
print(rem_redundant_el_from_list1(LIST_OF_LISTS))
print(rem_redundant_el_from_list2(LIST_OF_LISTS))
print(rem_redundant_el_from_list3(LIST_OF_LISTS))

#3
def find_the_highest_list(list_n):
    """Function"""
    temp = 0
    for n in list_n:
        if temp < sum(n):
            temp = sum(n)
            highest_list = n
    return highest_list

print(find_the_highest_list([[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]))

def get_l_w_max_sum(l_of_lists):
    """Function"""
    return max([(l, sum(l)) for l in l_of_lists], key=lambda x: x[1])[0]


LIST3 = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]

print(get_l_w_max_sum(LIST3))


#4
def compute_similarity(list_one, list_two):
    """Function"""
    return [n for n in list_one if not n in list_two]

print(compute_similarity(["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]))

def lists_similarity(l1, l2):
    """Function """
    return list(set(l1) - set(l2)), list(set(l2) - set(l1))

#5
def change_position(args):
    """Function """
    for i in range(0, len(args)-1, 2):
        prev = args.index(args[i])
        args.insert(prev + 1, args.pop(prev))
    return args

print(change_position([0, 1, 2, 3, 4, 5]))



#6
def sort_tuples(l_of_tuples):
    """Function """
    return sorted(l_of_tuples, key=lambda t: t[1])

print(sort_tuples([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


#7
def count_number_of_strings(l_of_str):
    """Function """
    return len([s for s in l_of_str if len(s) >= 2 and s[0] == s[-1]])

print(count_number_of_strings(['abc', 'xyz', 'aba', '1221']))



#TUPLE
#8
def tuple_with_string(t):
    """Function """
    return "This is a tuple {}".format(t)

print(tuple_with_string((100, 200, 300)))

#9
def tuple_replace_last(l_of_tuples):
    """Function """
    return [t[:-1] + (new_el,) for t in l_of_tuples]

print(tuple_replace_last([(10, 20, 40), (40, 50, 60), (70, 80, 90)]))

#10
def remove_empty_tup(l_of_tuples):
    """Function """
    return [t for t in l_of_tuples if t]

print(remove_empty_tup([(), (), ('',), ('a', 'b'), ('a','b', 'c'), ('d')]))

#11
def sort_by_float(l_of_tuples):
    """Function """
    return sorted(l_of_tuples, key=lambda t: t[1], reverse=True)

print(sort_by_float([('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]))

#SET
#12
def shallow_copy(args):
    """Function """
    return args.copy()

print(shallow_copy(set(["Green", "Red"])))

#13
def remove_from_set(origin_set, el_to_del):
    """Function """
    origin_set.discard(el_to_del)
    return origin_set

print(remove_from_set(1, set([1, 2, 3])))

#DICT
#14
def print_unique(l_of_dicts):
    """Function """
    set_of_values = set(itertools.chain(*[d.values() for d in l_of_dicts]))
    return 'Unique Values: {}'.format(set_of_values)

print_unique([{"V":"S001"}, {"V":"S002"}, {"VI":"S001"}, {"VI":"S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}])

#15
def combination_of_letters(dict):
    """Function """
    for c in itertools.product(*dic.values()):
        print(''.join(c))

print(combination_of_letters({'1':['a','b'], '2':['c','d']}))

#16
def string_to_dict(string):
    """Function """
    return dict(Counter(string))

print(string_to_dict("w3resource"))

#17
def top_three(dic):
    """Function """
    for t in sorted(dic.items(), key=lambda t: t[1], reverse=True)[:3]:
        print('{} {}'.format(t[0], t[1]))

print(top_three({'item1':45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}))

#18
def create_dictionary(l1, l2):
    """Function """
    return {k: {v} for k, v in (zip(l1, l2))}

print(create_dictionary(['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]))

#19
def match_keys(dict1, dict2):
    """Function """
    set_items1 = set(dic1.items())
    set_items1.intersection_update(set(dic2.items()))
    for same_item in set_items1:
        print('{0}: {1} is present in both x and y'.format(*same_item))

match_keys({'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2})

#FUNC
#20 and 21
def sum_el_in_list(args):
    """Function """
    return sum(args)

print(sum_el_in_list([8, 2, 3, 0, 7]))

#22
def sort_words_with_hyphen(string):
    """Function """
    return '-'.join(sorted(string.split('-')))

print(sort_words_with_hyphen("green-red-yellow-black-white"))

#23
def is_number_perfect(number):
    """Function """
    if number > 0 and isinstance(number, int):
        temp = []
        for n in range(1, number):
            if number % n == 0:
                temp.append(n)
        return sum(temp) == number
    else:
        return "The number has to be positive integer"

print(is_number_perfect(8128))

#24
def get_even_numbers(list_n):
    """Function """
    return [n for n in list_n if n % 2 == 0]

print(get_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))
