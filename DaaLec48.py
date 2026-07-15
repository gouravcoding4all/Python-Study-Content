Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
"""
7.Bitwise Operator
and -> &
or  -> |
not -> ~
"""
'\n7.Bitwise Operator\nand -> &\nor  -> |\nnot -> ~\n'
a=19
b=42
print(a | b)  #59
59
print(a & b)  #2
2
# first convert first bitwise into operand into binary code then apply operator.
a=24
b=49
print(a|b)  #59
57
print(a&b)  #2
16
print(a&b)  #16
16
print(a|b)  #57
57
#not ~
#input => -(x+1)
a=6
print(~a)
-7
a=-17
print(~a)
16
#XOR ^:In XOR if both/all inputs are same ,then result is FALSE Otherwise TRUE
a=7
b=5
print(a^b)
2
>>> 
>>> #a=7=>111
>>> #b=5=>101
>>> #a^b => 010 => 2
>>> 
>>> a=7
>>> b=2
>>> print( a^b )
5
>>> #a=7 => 111
>>> #b=5 => 101
>>> #b=2 => 010
>>> #a^b => 101 => 5
>>> 
>>> #left shift operator <<
>>> #right shift operator >>
>>> 
>>> a=29
>>> print(a>>1) #14
14
>>> print(a<<2)
116
>>> print(a>>2)
7
>>> print(a>>3) #3
3
>>> 
>>> a=7
>>> print(a<<1)
14
>>> print(a<<2)
28
>>> print(a<<3)
56
>>> """
... Quess_Question
... Q3
... print(4 ** 0 ** 2) 
... # (4**0)**2
... # 1**2
... # 1


Q5
print((3 and 0) or (0 and 3)) 
# 0 or 0
# 0


Q11
print(1 << 2 + 1)
# 1 << 2+1
# 1<<3
# 8


print(3 < 5 > 2 == 2)
# 3<5 and 5>2 and 2==2
# True and True and True
# True

x = 10 
y = 20 
print(x & y | x ^ y)
# x = 10 => 01010
# y = 20 => 10100
# x&y    => 00000
# x&y|x  => 01010
# ^y     => 11110  => 30


print((not 0) * (False or 1)) 

# True * True
# 1 * 1
# 1

"""
'\nQuess_Question\nQ3\nprint(4 ** 0 ** 2) \n# (4**0)**2\n# 1**2\n# 1\n\n\nQ5\nprint((3 and 0) or (0 and 3)) \n# 0 or 0\n# 0\n\n\nQ11\nprint(1 << 2 + 1)\n# 1 << 2+1\n# 1<<3\n# 8\n\n\nprint(3 < 5 > 2 == 2)\n# 3<5 and 5>2 and 2==2\n# True and True and True\n# True\n\nx = 10 \ny = 20 \nprint(x & y | x ^ y)\n# x = 10 => 01010\n# y = 20 => 10100\n# x&y    => 00000\n# x&y|x  => 01010\n# ^y     => 11110  => 30\n\n\nprint((not 0) * (False or 1)) \n\n# True * True\n# 1 * 1\n# 1\n\n'
