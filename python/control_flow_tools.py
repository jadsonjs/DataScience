#
# https://docs.python.org/3/tutorial/
#
# to execute this file type:  "python3 control_flow_tools.py" on linux or macoc terminal
#


#if Statements

x = int( input("Please enter an integer: ") )

if x < 0:
	print('Negative')
elif x == 0:
     print('Zero')
elif x == 1:
     print('Single')
else:
     print('Positive')




#for Statements


words = ['cat', 'window', 'defenestrate']
for w in words:
     print(w, len(w))



for i in range(5):
	print(i)

# To iterate over the indices of a sequence, you can combine range() and len() as follows
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
	print(i, a[i])


# the else clause belongs to the for loop, not the if statement
# a loop’s else clause runs when no break occurs.
for n in range(2, 10):
     for x in range(2, n):
         if n % x == 0:
             print(n, 'equals', x, '*', n//x)
             break
     else:
         # loop fell through without finding a factor
         print(n, 'is a prime number')


