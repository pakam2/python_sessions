from typing import List
#Type hinting with alias
Vector = List[int]
def return_value(val: Vector) -> Vector:
    return [val, (val + 1)]

#Formating
print("Hello %s" % "World!")
print("Hello {}".format("World!"))
print("{} {}".format("Hello", "World!"))
print("Hello {World}".format(World="World!"))

#Variable declaration and naming
#immutable
text_value = "Hello World!"
number_value = 1
tuple_value = (1, 2)
#mutable
list_value = [1, 2]
dict_value = {"key": "value"}

#Multi-Line Statements
message\
=\
'This \
back slash \
acts \
like \
enter'
print(message)

#Comments
# First comment
print ("Hello, Python!") # second comment
