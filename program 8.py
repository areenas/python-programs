#!/usr/bin/env python
# coding: utf-8

# In[3]:


year = int(input("enter the year : "))
if(year % 400 == 0)and(year % 100 == 0):
    print("leap year")
    if(year % 4 == 0)and( year % 100 != 0):
            print("leap year")
else:
        print("not a leap year")


# In[ ]:





# In[ ]:




