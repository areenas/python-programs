# -*- coding: utf-8 -*-
"""Untitled29.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ApI6d0Dzl2jGfh1cuNxVhFq0Y1gvhL_D
"""

lis=[]
lim=int(input("enter the limit of student:"))
for i in range(lim):
  name=input("enter the name:")
  marks=int(input("enter the rollno:"))
  attendance=int(input("enter the attendance:"))
  student={"name":name,"rollno":marks,"attendance":attendance}
  lis.append(student)
print(lis)