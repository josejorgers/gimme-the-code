import sys
sys.path.insert(0, 'C:\\Users\\JJ\\Desktop\\gimme-the-code\\')
from gtcode.extract import get_python_code

s =\
'''
The following code shows an example of for loop
in python.

for i in range(10):
    print(i)

class Example(Base):

    def __init__(self, a, b,
                        c, e):
        self.a = a

    def sum_with_bl():
        return\
            a + b

## OUTPUT:
# 0
# 1
# 2
# 3
# ...
# 9

That's it!
'''

c =\
'''
for i in range(10):
    print(i)

class Example(Base):
    def __init__(self, a, b,
                        c, e):
        self.a = a
    def sum_with_bl():
        return\
            a + b
            
## OUTPUT:
# 0
# 1
# 2
# 3
# ...
# 9
'''
def test_get_python_code():

    code = get_python_code(s)

    # assert c == code
    print(code)
    print('===============')
    print(c)

    for i in range(len(code)):
        if code[i] != c[i]:
            print('MISSMATCH:', i)
            print(code[i])
            print(c[i])
