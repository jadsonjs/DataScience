
#
# https://docs.python.org/3/tutorial/
#
# to execute this file type:  "python3 basic.py" on linux or macoc terminal
#

# simple comment

""" 
   Several 
   lines 
   comments
"""

# numbers 
print(2 + 2)

print((50 - 5 * 6) / 4)

print(17 / 3)  # classic division returns a float

print(17 // 3)  # floor division discards the fractional part

print(17 % 3)  # the % operator returns the remainder of the division


# Strings

word = 'Python'
print(word[0])  # character in position 0

word2 = "Python"
print(word2) 

word3 = ' He said: "hello" '
print(word3) 

print(word[2:5])  # characters from position 2 (included) to 5 (excluded)


s = 'supercalifragilisticexpialidocious'
print(len(s))


#Lists


squares = [1, 4, 9, 16, 25]
print(squares)



print( squares + [36, 49, 64, 81, 100] )  # concatenation


squares[0] = 2  # change a element of a list
print(squares)

print(len(squares))


