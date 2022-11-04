#!/usr/bin/env python
# coding: utf-8

# In[3]:


num=int(input("Enter the number :"))
n=num
sum=0
a=len(str(num))
while n>0:
    d=n%10
    sum=sum+(d**a)
    n=n//10
if(num==sum):
    print(num," is a armstrong number ")
else:
    print(num,"is not a armstrong number")


# In[ ]:





# In[ ]:





# In[ ]:




