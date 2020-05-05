"""
CTEC 121
Frank Dvorak
Mod 2 Programming Assignment
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

import math
def main():
    '''
    # section 1
    print("\nSection 1")
    # create three variables of different types
    myInt = 123
    myFloat = 3.14
    myStr = "my string"
    # print values
    print("\tmyInt:\t", myInt) #print(arg1, arg2, arg3)
    print("\tmyFloat:", myFloat)
    print("\tmyStr:\t", myStr)
    print()
    # section 2
    print("Section 2 and 3")
    # demo sep
    print("\tusing default")
    print("\tone", "two", "three")
    print("\tsep=\'-\'")
    print("\tone", "two", "three", sep="-")
    print("\tend=\' \'")
    print("\tone", "two", "three", end=" ")
    print("one", "two", "three")
    print("\tdemo backslash escape character: path=c:\\folder\\folder\\filename")
    print()
    ze = 4968054798 / 0
    print(ze)
ZeroDivisionError: division by zero
'''
    print("test")

    a = math.sqrt(387)
    y = 456
    r = 212
    x = 4 * math.pi / math.cosh(y) + r**3
    z = x + y
    z1 = x + y / math.ceil(a)
    b = a + z * math.floor(4587.33336)
    v = 4 / 3 * math.pi**3
    e = 4 * math.pi * r**2
    f = math.sin(r) * math.pi**3

 

    print()
    print(a)
    print(x)
    print(z1)
    print(b)
    print(v)
    print(y**2)
    print(r**3)
    print(a+y+r+z+z1+b+v+e)
    print(f+e)
    print(f+e / math.tan(z))
main()


   