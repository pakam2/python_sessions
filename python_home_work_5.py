#1, 2
class ConvertNumber():

    def convert_integer_to_roman(self, number_int):
        roman = number_int
        ints = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_num = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res= ''
        i = 0
        while  number_int > 0:
            for n in range(number_int // ints[i]):
                res += roman_num[i]
                number_int -= ints[i]
            i += 1
        return "Roman {} is arabic {}".format(res, roman)

    def convert_roman_to_int(self, roman_number):
        roman = roman_number
        roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        number_value = 0
        for i in range(len(roman_number)):
            if i > 0 and roman_num[roman_number[i]] > roman_num[roman_number[i - 1]]:
                number_value += roman_num[roman_number[i]] - 2 * roman_num[roman_number[i - 1]]
            else:
                number_value += roman_num[roman_number[i]]
        return "Arabic {} is roman {}".format(number_value, roman)

ConvertNumberIntRoman = ConvertNumber()
print("Ex. 1, 2: " + str(ConvertNumberIntRoman.convert_integer_to_roman(1)))
print("Ex. 1, 2: " + str(ConvertNumberIntRoman.convert_integer_to_roman(55)))
print("Ex. 1, 2: " + str(ConvertNumberIntRoman.convert_roman_to_int("I")))
print("Ex. 1, 2: " + str(ConvertNumberIntRoman.convert_roman_to_int("LV")))


#3
class CheckParenthese():
   def check_parenthese(self, parenthese_seq):
        empty = []
        p_keys_values =  {"(": ")", "{": "}", "[": "]"}
        for parenthese in parenthese_seq:
            if parenthese in p_keys_values:
                empty.append(parenthese)
            elif len(empty) == 0 or p_keys_values[empty.pop()] != parenthese:
                return False
        return len(empty) is 0

C = CheckParenthese()
print("Ex. 3: " + str(C.check_parenthese('(){}[]')))
print("Ex. 3: " + str(C.check_parenthese('([]')))


#4
class Create_subset():
    def get_subset(self, res, number_set):
        if number_set:
            return self.get_subset(res, number_set[1:]) + self.get_subset(res + [number_set[0]], number_set[1:])
        return [res]

C = Create_subset()
print("Ex. 4: " + str(C.get_subset([], sorted([4,5,6]))))


#5
class SumNumber():

    def find_numbers(self, numbers, target):
        i = 0
        j = 1
        flag = False
        while flag == False:
            sum = 0
            for n in numbers[i:j + 1]:
                sum += n
                if sum == target:
                    flag = True
                    return [i + 1, j + 1]
            i += 1
            j += 1


print("Ex. 5: " + str(SumNumber().find_numbers([10,20,10,40,50,60,70] , 50)))
print("Ex. 5: " + str(SumNumber().find_numbers([10,20,10,40,50,60,70] , 30)))


#6
class SumZero:

    res = []

    def sum_three_numbers_to_zero(self, numbers):
        numbers = sorted(numbers)
        i = 0
        while i < len(numbers) - 2:
            j = i + 1
            k = len(numbers) - 1
            while j < k:
                firstSum = numbers[i] + numbers[j] + numbers[k]
                if firstSum < 0:
                    j += 1
                elif firstSum > 0:
                    k -= 1
                else:
                    SumZero.res.append([numbers[i], numbers[j], numbers[k]])
                    j += 1
                    k =- 1
                    while j < k and numbers[j] == numbers[j - 1]:
                        j += 1
                    while j < k and numbers[k] == numbers[k + 1]:
                        k -= 1
            i += 1
            while i < len(numbers) - 2 and numbers[i] == numbers[i - 1]:
                i += 1
        return sorted(SumZero.res)
print("Ex. 6: " + str(SumZero().sum_three_numbers_to_zero([-25, -10, -7, -3, 2, 4, 8, 10])))


#7
class Power():
   def m_pow(self, num, p):
        if num <= 1 or p == 1:
            return num

        if num == -1:
            if p % 2 == 0:
                return 1
            else:
                return -1
        #if 'p' is negative
        res = self.m_pow(num, p // 2)
        if p % 2 == 0:
            return res * res
        return res * res * num

print("Ex. 7: " + str(Power().m_pow(1, -4)))
print("Ex. 7: " + str(Power().m_pow(2, 5)))

#8
class ChangeOrder():
    def change_order_of_words(self, word_list=[]):
        return ' '.join(reversed(word_list))

print("Ex. 8: " + ChangeOrder().change_order_of_words('hello .py'.split()))


#9
class StringClass():

    def get_string(self, input):
        self.input = input

    def print_string(self):
        return self.input.upper()

C = StringClass()
C.get_string('asdfasdfa')
print("Ex. 9 " + C.print_string())

#10
class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width  = width

    def calc_area(self):
        return self.length * self.width

R = Rectangle(4, 20)
print("Ex. 10. Area of rectangle: " + str(R.calc_area()))

#11, 12
class Circle():

    PI = 3.14
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return self.radius ** 2 * Circle.PI

    def calc_perimeter(self):
        return 2 * self.radius * Circle.PI

C = Circle(10)
print("Ex. 11. Area of circle: " + str(round(C.calc_area(), 2)))
print("Ex. 11. Perimeter of circle: " + str(round(C.calc_perimeter(), 2)))
