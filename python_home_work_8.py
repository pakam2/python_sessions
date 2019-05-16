"""Homework 8"""
#In the whole file I used short names for variables (only for time saving purpose)
import enum
import binascii
import heapq
import bisect
import queue
from collections import Counter, defaultdict, OrderedDict
from array import array

#1
class SampleData(enum.Enum):
    """Example of Enum implementation"""
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    AngolaTwo = 244
    Antarctica = 672
    aaa = 672
#2
for n in SampleData:
    print('{} = {}'.format(n.name, n.value))
#3
Container = [n.name for n in SampleData]
print(sorted(Container))
#4
print([n.value for n in SampleData])

#5
def count_words(list_words):
    """Function to count words"""
    count = Counter(list_words)
    return count.most_common(4)

#6
def class_wise_roll(tup_l):
    """Function for wise roll"""
    roll = defaultdict(list)
    for n, id in tup_l:
        roll[n].append(id)
    return roll

#7
classes = (
    ('V', 1),
    ('VI', 1),
    ('V', 2),
    ('VI', 2),
    ('VI', 3),
    ('VII', 1),
)
def count_number_of_students(classes):
    """Function for counting students"""
    return Counter(name for name, num in classes)

#8
for n in SampleData:
    print('{} = {}'.format(n.name, n.value))

#9
dict2 = {'Afghanistan': 93, 'Albania': 355, 'Algeria': 213, 'Andorra': 376, 'Angola': 244}
ord_dict = OrderedDict(dict2.items())
for k in ord_dict:
    print(k, ord_dict[k])

for k in reversed(ord_dict):
    print(k, ord_dict[k])


#10
def group_seq_k_v(l):
    """Function for grouping sequence"""
    d = defaultdict(list)
    for k, v in l:
        d[k].append(v)
    return d

#11
def compare_lists(a, b):
    """Function to compare list"""
    return a == b

#12
def create_array(list_of_int):
    """Function to create an array"""
    arr = array('i', list_of_int)
    return arr


#13
def size_of_array(int_or_float, num_tup):
    """Function to get size of array"""
    a = array(int_or_float, num_tup)
    return a.itemsize

#14
def array_buffer_info(num_tup):
    """Function to get the buffer info"""
    a = array("I", num_tup)
    return a.buffer_info()

#15
def len_of_array(arr):
    """Function to get the length of array"""
    a = array('i', arr)
    return len(a)

#16
def convert_array_to_list(arr):
    """Function to convert an array to list"""
    a = array('i', arr)
    return a.tolist()

#17
def array_to_bytes(arr):
    """Function to get byte representation of array"""
    a = array('i', arr)
    arr_bytes = a.tobytes()
    return binascii.hexlify(arr_bytes)

#18
array1 = array('i', [7, 8, 9, 10])
print('array1:', array1)
bytes2 = array1.tobytes()
print('Bytes:', binascii.hexlify(bytes2))
array2 = array('i')
array2.frombytes(bytes2)
print('array2:', array2)

#19
def print_heap(h):
    """Function to print a heap"""
    heap = []
    for n in h:
        heapq.heappush(heap, n)
    for x in heap:
        print(x)
    return heap
#20
def smallest_in_heap(h):
    """Function to get the smallest element in heap"""
    heap = []
    for n in h:
        heapq.heappush(heap, n)
    print("Items in the heap:")
    for a in heap:
	    print(a)
    print("The smallest item in the heap:")
    print(heap[0])
    print("Pop the smallest item in the heap:")
    heapq.heappop(heap)
    for a in heap:
	    print(a)
    return heap

#21
def pop_from_heap(h):
    """Function to pop from heap"""
    heap = []
    for n in h:
        heapq.heappush(heap, n)

    heapq.heappushpop(heap, ('V', 6))
    for a in heap:
    	print(a)
#22
def heapsort(h):
    """Function sort heap"""
    heap = []
    for value in h:
        heapq.heappush(heap, value)
    return [heapq.heappop(heap) for i in range(len(heap))]

#23
def large_small(h, largest=2, smallest=3):
    """Function to get the largest and smallest"""
    l = heapq.nlargest(largest, h)
    s = heapq.nsmallest(smallest, h)
    print(l)
    print(s)
    return l + s

#24
def insert_left(num, x):
    """Function to insert to left"""
    return bisect.bisect_left(num, x)

#25
def insert_right(num, x):
    """Function to insert to right"""
    return bisect.bisect_right(num, x)

#26
def sort_list(l):
    """Function to insert sort"""
    sorted_l = []
    for i in l:
        bisect.insort(sorted_l, i)
    return sorted_l
#27
def create_queue(el_in_q):
    """Function to create queue"""
    mq = queue.Queue()
    for x in range(el_in_q):
        mq.put(x)
    print("Members of the queue:")
    return mq.qsize()

#28
def is_queue_empty(q):
    """Function to check if the queue is empty"""
    return q.empty()

#29
class FIFOQ():
    """class that is an implementation of FIFO queue"""
    def __init__(self, num):
        self.q = queue.Queue()
        for n in range(num):
            self.q.put(str(n))

    def remove_all_items(self):
        """Remove all items and return True"""
        while not self.q.empty():
            print(self.q.get())
        return True

#30
class LIFOQ():
    """class that is an implementation of LIFO queue"""
    def __init__(self, num):
        self.q = queue.LifoQueue()
        for n in range(num):
            self.q.put(str(n))

    def remove_all_items(self):
        """Remove all items and return True"""
        while not self.q.empty():
            print(self.q.get())
        return True
