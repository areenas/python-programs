# -*- coding: utf-8 -*-
"""Untitled25.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eV1mgSMdKAIroRz2As68YvIjcPXIzbTL
"""

n=int(input("Enter the number of students:"))
studentlist=[]
for i in range(0,n):
    student={}
    student["name"]=input("Enter the name:")
    student["roll no"]=int(input("Enter the roll number:"))
    student["mark"]=int(input("Enter the mark:"))
    studentlist.append(student)
print("Marklist:")
for i in range(1,n):
    for j in range(0,n-1):
        if(studentlist[j]["mark"]<studentlist[j+1]["mark"]):
            temp=studentlist[j]
            studentlist[j]=studentlist[j+1]
            studentlist[j+1]=temp
           
for i in range(0,n):
        print(studentlist[i])