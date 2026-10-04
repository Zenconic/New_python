a = [1,2,3]
b = [1,2,3]
c = a

print(a is b) #false
print(a == b) #true
print(a is c) #true
print(id(a)) # prints the memory of a
print(id(b)) # prints the memory of b
print(id(c)) # prints the memory of c

# Arithmetic
print(5 + 3) # 8 addition
print(10 - 3) # 7 subtraction
print(3 * 4) # 12 multiplication
print(7 / 2) # 3.5 division (always float)
print(4 / 2) # 2.0 float, NOT 2
print(7 // 2) # 3 floor division (rounds DOWN)
print(17 // 5) # 3
print(-17 // 5) # -4 rounds toward negative infinity, not zero
print(-7 // 2) # -4
print(7 % 3) # 1 remainder
print(17 % 5) # 2 (17 = 3*5 + 2)
print(10 % 2) # 0 even number -> no remainder
print(7 % 2) # 1 odd number
print(2 ** 10) # 1024 power
print(64 ** 0.5) # 8.0 square root
print(27 ** (1/3)) # 3.0 cube root
print("Hi " + "there") # Hi there (joins strings)
print("ab" * 3) # ababab (repeats string)
print([1, 2] * 2) # [1, 2, 1, 2] (repeats list)

# Comparison
print(5 == 5) # True equal to
print(5 != 3) # True not equal to
print(7 > 3) # True greater than
print(3 < 7) # True less than
print(5 >= 5) # True greater or equal
print(4 <= 5) # True less or equal
print(10 > 20) # False

x = 5
print(1 < x < 10) # True chained comparison
print(0 <= x <= 5) # True
print(5 < x < 10) # False

print("apple" < "banana") # True ('a' = 97, 'b' = 98)
print("Python" == "python") # False case-sensitive
print(1 == True) # True
print(0 == False) # True
print(1 == "1") # False int vs str

# Assignment
x = 5 # assign
x += 3 # x = x + 3
print(x) # 8
x -= 2 # x = x - 2
print(x) # 6
x *= 4 # x = x * 4
print(x) # 24
x /= 2 # x = x / 2
print(x) # 12.0
x = 20
x //= 3 # x = x // 3
print(x) # 6
x %= 4 # x = x % 4
print(x) # 2
x **= 5 # x = x ** 5
print(x) # 32

a = b = c = 0 # multiple assignment
print(a, b, c) # 0 0 0
x, y, z = 1, 2, 3 # tuple unpacking
print(x, y, z) # 1 2 3
a, b = 10, 20
a, b = b, a # swap
print(a, b) # 20 10

# Logical 
age = 20
has_id = True
print(age >= 18 and has_id) # True both must be True
is_student = True
is_teacher = False
print(is_student or is_teacher) # True at least one True
print(not True) # False
print(not False) # True

print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False
print(True or False) # True
print(False or False) # False

print(False and 1/0) # False short-circuit, no error
print(True or 1/0) # True short-circuit, no error

marks = 72
print(marks >= 40 and marks <= 100) # True
print(marks < 40 or marks > 100) # False

# Bitwise
print(bin(5)) # 0b101
print(bin(3)) # 0b11
print(int('0101', 2)) # 5
print(5 & 3) # 1 AND (0101 & 0011 = 0001)
print(5 | 3) # 7 OR (0101 | 0011 = 0111)
print(5 ^ 3) # 6 XOR (0101 ^ 0011 = 0110)
print(~5) # -6 NOT = -(5 + 1)
print(5 << 1) # 10 left shift (x2)
print(5 << 2) # 20 left shift (x4)
print(20 >> 1) # 10 right shift (/2)
print(20 >> 2) # 5 right shift (/4)
print(5 >> 1) # 2

# Membership
print("py" in "python") # True
print("Java" in "python") # False
print("z" not in "hello") # True
print("a" in "apple") # True
print("x" not in "apple") # True
print(2 in [1, 2, 3]) # True
print(5 not in (1, 2, 3)) # True

# Identity
a = [1,2,3]
b = [1,2,3]
c = a

print(a is b) # False different objects
print(a == b) # True same values
print(a is c) # True same object
print(a is not b) # True
print(id(a))
print(id(b))
print(id(c))

x = None
print(x is None) # True correct way
print(x == None) # True works, not recommended
print(x is not None) # False

# Precedence 
print(2 + 3 * 4) # 14 * before +
print((2 + 3) * 4) # 20 parentheses first
print(2 ** 3 ** 2) # 512 ** is right to left
print((2 ** 3) ** 2) # 64
print(5 > 3 and 2 < 4) # True comparisons first, then and
print(not True or True) # True not binds tighter than or
result = (5 + 3) * (10 - 4)
print(result) # 48