#!/usr/bin/env python
# coding: utf-8

# In[5]:


num=int(input("Enter a number:"))
flag=False
for i in range (2,num):
    if(num % i==0):
        flag=True
        break
if flag:
    print(num,"is not a prime number")
else:
    print(num,"is a prime number")


# In[ ]:




