# Ref: https://www.youtube.com/watch?v=qUeud6DvOWI

from collections import namedtuple

# Passing variable into string
def string_formatting(name, age):
    print(f"My name is {name}. I am {age} years old")

# Writing to a file
def calling_close_on_a_file(filename):
    with open(filename, "w") as f:
        f.write("hello!")

# Always specify type of error in Except part
def bare_except():
    while True:
        try:
            s = input("Input a number: ")
            x = int(s)
            break
        except Exception:
            print("Not a number, try again")


def caret_and_exponentiation(x, p):
    y = x^p
    print(y)
    y = x ** p
    print(y)


def appends(n, l=None):
    if l is None:
        l = []
    l.append(n)
    return l

def using_comprehensions():
    dict_comp = {i:i * i for i in range(10)}
    list_comp = [i for i in range(10)]
    print(dict_comp)
    print(list_comp)


def checking_type_equality():
    Point = namedtuple('Point', ['x','y'])
    p = Point(1,2)
    print(p)

    if isinstance(p, tuple):
        print("it's a tuple")
    else:
        print("it's not a tuple")

if __name__ == '__main__':
    string_formatting("Azfar", 14)
    calling_close_on_a_file("test.txt")
    #bare_except()
    l3 = appends(0)
    l4 = appends(1)
    print(l3, l4)
    using_comprehensions()
    checking_type_equality()