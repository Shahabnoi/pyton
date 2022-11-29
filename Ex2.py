# Constants
print(123) 
print(98.6)
print('Hello world')

# Assignment
x = 2
x = x + 2
print(x)

# Order of Evaluation
x = 1 + 2 * 3 - 4 / 5 ** 6
print(x)
x = (1 + 2)* 3 - 4 / 5 ** 6
print(x)
x = 1 + (2 * 3) - 4 / 5 ** 6
print(x)
x = (1 + 2 * 3 - 4 / 5) ** 6
print(x)
x = 1 + (2 * 3 - (4 / 5)) ** 6
print(x)

# Type Matters
eee = 'hello ' + 'there'
eee = eee + 1

# typeConversions
print(float(99) + 100)
199.0
i = 42
type(i)
f = float(i)
print(f)
42.0
type(f)
sval = '123'
type(sval)

# convert
nsv = 'hello bob'
niv = int(nsv)

# User Input
name = input('Who are you? ')
print('Welcome', name)

# Converting User Input
inp = input('Europe floor?')
usf = int(inp) + 1
print('US floor', usf)



# Conditional Steps
x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')

print('Finis')

# Comparison Operators
x = 5
if x == 5 : 
    print('Equals 5')
if x > 4 : 
   print('Greater than 4')
if  x >= 5 :
    print('Greater than or Equals 5')
if x < 6 : print('Less than 6') 
if x <= 5 :
    print('Less than or Equals 5')
if x != 6 :
    print('Not equal 6')

