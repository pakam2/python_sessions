"""Module for testing"""
from python_home_work_8 import *
import unittest

def fun(x):
    return x + 1

class TestHomeWork(unittest.TestCase):
    """Testing for homework part 8"""

    def test_sample_data_check_name(self):
        afg = SampleData.Afghanistan.name
        self.assertEqual(afg, 'Afghanistan')

    def test_sample_data_check_value(self):
        afg_value = SampleData.Afghanistan.value
        self.assertEqual(afg_value, 93)

    def test_count_words(self):
        list_words = [ 'orange', 'pink', 'pink', 'red', 'red', 'white', 'orange', 'black']
        self.assertEqual(count_words(list_words), [('orange', 2), ('pink', 2), ('red', 2), ('white', 1)])

    def test_class_wise_roll(self):
        l = (('I', 32), ('V', 5), ('VII', 2), ('VI', 2))
        self.assertEqual(class_wise_roll(l), {'I': [32], 'V': [5], 'VII': [2], 'VI': [2]})

    def test_count_number_of_students(self):
        classes = (
            ('V', 1),
            ('VI', 1),
            ('V', 2),
            ('VI', 2),
            ('VI', 3),
            ('VII', 1),
        )
        self.assertEqual(count_number_of_students(classes), {'VI': 3, 'V': 2, 'VII': 1})

    def test_group_seq_k_v(self):
        l = [('v', 1), ('v', 3), ('vii', 1), ('vi', 4), ('vi', 2)]
        self.assertEqual(group_seq_k_v(l),  {'v': [1, 3], 'vii': [1], 'vi': [4, 2]})

    def test_compare_lists(self):
        list_one = [1, 2, 3]
        list_two = [1, 2 ,3]
        list_three = [1, 2, 4]
        self.assertEqual(compare_lists(list_one, list_two), True)
        self.assertEqual(compare_lists(list_one, list_three), False)

    def test_create_array(self):
        self.assertEqual(create_array([10, 20, 30, 40, 50]), array('i',[10, 20, 30, 40, 50]))

    def test_large_small(self):
        self.assertEqual(large_small([4, 5, 6, 78, 1, 3]), [78, 6, 1, 3, 4])

    def test_size_of_array(self):
        self.assertEqual(size_of_array('I', (432, 22)), 4)
        self.assertEqual(size_of_array('f', (1.2, 3.3)), 4)

    def test_len_of_array(self):
        self.assertEqual(len_of_array([1, 2, 3, 4, 5]), 5)

    def test_convert_array_to_list(self):
        self.assertEqual(convert_array_to_list([1, 2, 3]), [1, 2, 3])

    def test_array_to_bytes(self):
        self.assertEqual(str(array_to_bytes([1, 2, 3, 4, 5])), str(b'0100000002000000030000000400000005000000'))

    def test_print_heap(self):
        self.assertEqual(print_heap([('V', 1), ('V', 2), ('V', 3)]), [('V', 1), ('V', 2), ('V', 3)])

    def test_smallest_in_heap(self):
        self.assertEqual(smallest_in_heap([('V', 1), ('V', 2), ('V', 3)]), [('V', 2), ('V', 3)])

    def test_heapsort(self):
        self.assertEqual(heapsort([50, 70, 90, 20,50, 40, 60, 80,100]), [20, 40, 50, 50, 60, 70, 80, 90, 100])

    def test_insert_left(self):
        self.assertEqual(insert_left([1, 2, 4, 5], 6), 4)

    def test_insert_rigth(self):
        self.assertEqual(insert_right([1, 2, 3, 4], 2), 2)

    def test_sort_list(self):
        self.assertEqual(sort_list([1, 4, 56, 7, 8]), [1, 4, 7, 8, 56])

    def test_create_queue(self):
        self.assertEqual(create_queue(4), 4)

    def test_is_queue_empty(self):
        self.assertEqual(is_queue_empty(queue.Queue()), True)

    def test_fifo(self):
        fifo = FIFOQ(4)
        self.assertEqual(fifo.remove_all_items(), True)

    def test_lifo(self):
        lifo = LIFOQ(4)
        self.assertEqual(lifo.remove_all_items(), True)

if __name__ == '__main__':
    unittest.main()
