#!/usr/bin/env python
# coding: utf-8

# # Assignment 2
# ## Date: 3/9/2023
# ### Name: NGUYEN NGOC TU ANH

# * Exercise 1

# In[4]:


x = 100
y = 29
z = (x+y)*3
print(z**2)


# * Exercise 2

# In[19]:


name = input('Give your name: ')
year_of_birth = input('Give your year of birth: ')
age = input('give your age: ')

age = int(age)

print('password: ', year_of_birth[-2:], name[:3], (age)**2, sep='')


# * Exercise 3

# In[20]:


a = int(input('Give first number: '))
b = int(input('Give second number: '))

if a%2==0 and b%2==0:
    print('Both number are even')
elif a%2!=0 and b%2!=0:
    print('Both number are odd')
else:
    print('One of the number is even')


# * Exercise 4

# In[25]:


n = int(input('Give an integer: '))
sum = 0
for i in range (n):
    sum += i
print('The sum was: ', sum)


# * Exercise 5

# In[17]:


import random
random_num = random.randint(0,10)

guessed_num = int(input('Player: '))
tries = 1

while (guessed_num != random_num):
    if(guessed_num > random_num):
        print('Try a smaller number')
    else:
        print('Try a greater number')
    tries += 1
    guessed_num = int(input('Player: '))

print("That'right! Number of tries: ", tries)        


# * Exercise 5 bonus

# In[1]:


import random

a = [1, 2]

for i in range(2):
 
    tries = 0
    player = 'Player'+ str((i+1))
    random_num = random.randint(0,10)
    guessed_num = int(input(f'{player} : '))
    tries = 1
    
    while (guessed_num != random_num):
        
        if(guessed_num > random_num):
            print('Try a smaller number')
        else:
            print('Try a greater number')
       
        guessed_num = int(input(f'{player} : '))
        tries += 1
        
    a[i] = tries   
    print("That'right! Number of tries: ", tries) 
    print('\n')

print(a[0], a[1])
if a[0] > a[1]:
    print('Player 2 win')
elif a[0] < a[1]:
    print('Player 1 win')
else:
    print('draw')


# In[ ]:




