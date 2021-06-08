#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Write a program to check if the user is elgible to vote or not


# In[1]:


age = int(input("Enter your age: "))
if age >= 18:
    print("You are elgible to vote")
if age < 18:
    print("You are not elgible to vote")


# In[2]:


age = int(input("Enter your age: "))
if age >= 18:
    print("You are elgible to vote")
if age < 18:
    print("You are not elgible to vote")


# In[ ]:


#Write a program  to check if the given number is positive or not


# In[3]:


number = float(input("Enter a number: "))
if number >= 0:
    print("The given number is positive")
else:
    print("The given number is negative")


# In[4]:


number = float(input("Enter a number: "))
if number >= 0:
    print("The given number is positive")
else:
    print("The given number is negative")


# In[ ]:


#Check the given number is odd or even, if it's even then check if it is also divisible by 4 or not


# In[5]:


n = int(input("Enter a number: "))
if(n % 2) == 0:
    print("The given number is even")
else:
    print("The given number is odd")
if((n % 4) == 0):
    print("The given number is even and divisible by 4")


# In[6]:


n = int(input("Enter a number: "))
if(n % 2) == 0:
    print("The given number is even")
else:
    print("The given number is odd")
if((n % 4) == 0):
    print("The given number is even and divisible by 4")


# In[8]:


n = int(input("Enter a number: "))
if(n % 2) == 0:
    print("The given number is even")
else:
    print("The given number is odd")
if((n % 4) == 0):
    print("The given number is even and divisible by 4")


# In[ ]:


#write a program to print student grade based on percentage


# In[9]:


x = float(input("Enter your marks: "))
if x <= 35:
    print("Fail")
if (x > 35) & (x <= 75):
    print("Pass")
if (x > 75) & (x <= 100):
    print("Passed with distinction")


# In[ ]:


#check the given year is leap year or not


# In[10]:


year = int(input("Enter the year: "))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))


# In[11]:


year = int(input("Enter the year: "))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))


# In[ ]:




