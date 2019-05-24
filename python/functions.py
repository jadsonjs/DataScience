#
# https://docs.python.org/3/tutorial/
#
# to execute this file type:  "python3 functions.py" on linux or macoc terminal
#


 # Defining Functions

def fib(n):    
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

fib(100)