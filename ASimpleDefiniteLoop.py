
############
"""
for mytemp in [5, 4, 3, 6, 2, 1] :
    print(mytemp)
print('Blastoff!')
print('Before')
for thing in [9, 41, 12, 3, 74, 15] :
     print(thing)
print('After')
"""
##########################
"""
friends = ['Joseph', 'Glenn', 'Sally', 'yavar']
for c in friends : 
   print('Happy New Year:', c)
print('Done!')
"""
#######################
"""
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num > largest_so_far :
      largest_so_far = the_num
   print(largest_so_far, the_num)

print('After', largest_so_far)

"""
#################
"""
zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + 1
    print(zork, thing)
print('After', zork)
"""
##############
"""
count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum / count)
"""
###########
"""
name = input('Enter:')
print(name)
apple = input('Enter:')
#x = apple - 10
x = int(apple) - 10
print(x)
"""
####
fruit = 'banana'
index = 0
while index < len(fruit): 
    letter = fruit[index]
    print(index, letter)
    index = index + 1



