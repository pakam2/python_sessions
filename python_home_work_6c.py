#1
raise RuntimeError('Raise an error')


#2
try:
    a = 5 /0
except ZeroDivisionError:
    print("Cannot divide by 0")



#3
class CustomeError(Exception):

    def __init__(self, text):
        self.text = text
