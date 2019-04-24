#LIST

#1
def are_dicts_empty(list_of_dicts):
    for n in list_of_dicts:
        if not n == {}:
            return False
    return True



print(are_dicts_empty([{}, {}, {}]))
print(are_dicts_empty([{1, 2}, {}, {}]))



#2
def remove_duplicates(n):
    new_list =[]
    for x in n:
        if not x in new_list:
            new_list.append(x)
    return new_list

print(remove_duplicates([[10,20], [40], [30, 56, 25], [10,20], [33], [40]]))



#3
def find_the_highest_list(list_n):
    temp = 0
    for n in list_n:
        if temp < sum(n):
            temp = sum(n)
            highest_list = n
    return highest_list

print(find_the_highest_list([[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]))

#4
def compute_similarity(list_one, list_two):
    return [n for n in list_one if not n in list_two]

print(compute_similarity(["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]))


#5
def change_position(args):
    for i in range(0, len(args)-1,2):
        np = args.index(args[i]) + 1
        args.insert(np, args.pop(args.index(args[i])))
    return args

print(change_position([0, 1, 2, 3, 4, 5]))



#6
def sort_tuples(args):
    args.sort(key=lambda tup: tup[1])
    return args

print(sort_tuples([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


#7
def count_number_of_strings(args):
    res = []
    for n in args:
        if len(n) >= 2:
            if n[0] == n[len(n) -1]:
                res.append(len(n) -1)
    return res

print(count_number_of_strings(['abc', 'xyz', 'aba', '1221']))



#TUPLE
#8
def tuple_with_string(t):
    return "This is a tuple {}".format(t)

print(tuple_with_string((100, 200, 300)))

#9
def tuple_replace_last(args):
    return [(n[0], n[1], 100) for n in args]

print(tuple_replace_last([(10, 20, 40), (40, 50, 60), (70, 80, 90)]))

#10
def remove_empty_tup(args):
    return [n for n in args if not n is ()]

print(remove_empty_tup([(), (), ('',), ('a', 'b'), ('a','b', 'c'), ('d')]))

#11
def sort_by_float(args):
    args.sort(key=lambda tup: tup[1])
    args.reverse()
    return args

print(sort_by_float([('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]))

#SET
#12
def shallow_copy(args):
    return args.copy()

print(shallow_copy(set(["Green", "Red"])))

#13
def remove_from_set(val, args):
    for n in val[0:3]:
        if val in args:
            args.remove(val)
    return args

print(remove_from_set(1, set([1, 2, 3])))

#DICT
#14
def print_unique(dictionary):
    res= []
    for di in dictionary:
        for v in di.values():
            res.append(v)
    print(set(res))

print_unique([{"V":"S001"}, {"V":"S002"}, {"VI":"S001"}, {"VI":"S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}])

#15
def combination_of_letters(dictionary):
    temp= []
    for v in dictionary.values():
        temp.append(v)
    res = []
    for n in temp[0]:
        for x in temp[1]:
            res.append(n + x)
    return res

print(combination_of_letters({'1':['a','b'], '2':['c','d']}))

#16
def string_to_dict(string):
    res = {}
    for n in string:
        if not n in res:
            res[n] = 1
    return res

print(string_to_dict("w3resource"))

#17
def top_three(dictionary):
    val = dictionary.values()
    val = sorted(val)
    val.reverse()
    res = []
    for k, v in dictionary.items():
        if n == v:
            res.append(k + " " + str(v))
    return res

print(top_three({'item1':45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}))

#18
def create_dictionary(l1, l2):
    res = dict(zip(l1, l2))
    for k, v in res.items():
        res[k] = {v}
    return res

print(create_dictionary(['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]))

#19
def match_keys(dict1, dict2):
    res = []
    for k, v in dict1.items():
        for k2, v2 in dict2.items():
            if k == k2 and v == v2:
                res.append(k + ": is present in both dictionaries")
    return res

print(match_keys({'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}))

#FUNC
#20 and 21
def sum_el_in_list(args):
    sum_val = 0
    for n in args:
        sum_val += n
    return sum_val

print(sum_el_in_list([8, 2, 3, 0, 7]))

#22
def sort_words_with_hyphen(string):
    res = string.split("-")
    res.sort()
    return "-".join(res)

print(sort_words_with_hyphen("green-red-yellow-black-white"))

#23
def is_number_perfect(number):
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
    return [n for n in list_n if n % 2 == 0]

print(get_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))
