# -*- coding: utf-8 -*-
"""Untitled30.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J7sEScyqYFbLitZMHKZ8E-XO8o_u9CxM
"""

f=input("Enter the filename:")
try:
  f1=open(f,"r")
except:
  print ("No file named",f)