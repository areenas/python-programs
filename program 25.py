# -*- coding: utf-8 -*-
"""Untitled18.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xcO56jALq_Gftns1-IS23xUhBVHqiBnp
"""

str1=input("Enter the string :")
s=str1[0]
for i in range(len(str1)):
    str1=str1.replace(str1[0],'$')
    str2=s+str1[1:]
print(str2)

