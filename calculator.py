# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 20:42:49 2020

@author: PC
"""

#kalkulator 

while True:
    
    print("\n\tChoose one option: ")
    print("\tAddition: enter |add|\n")
    print("\tSubtraction: enter |sub|\n")
    print("\tMultiplication: enter |mlt|\n")
    print("\tDivision: enter |div|\n")
    print("\tExponentation: enter |exp|\n")
    print("\tExit: enter |exit|")
    user=input("chosen operation: ")
    if user=="exit":
        break
    elif user=="add":
        num_1=float(input("Enter the first number: "))
        num_2=float(input("Enter the second number: " ))
        add=num_1+num_2
        print(add)
    elif user=="sub":
        num_1=float(input("Enter the first number: "))
        num_2=float(input("Enter the second number: " ))
        sub=num_1-num_2
        print(sub)
    elif user=="mlt":
        num_1=float(input("Enter the first number: "))
        num_2=float(input("Enter the second number: " ))
        mlt=num_1*num_2
        print(mlt)
    elif user=="div":
        num_1=float(input("Enter the first number: "))
        num_2=float(input("Enter the second number: " ))
        div=num_1/num_2
        print(div)
    elif user=="exp":
        num_1=float(input("Enter the first number: "))
        num_2=float(input("Enter the second number: " ))
        exp=num_1**num_2
        print(exp)