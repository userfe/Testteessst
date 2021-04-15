# -*- coding: utf-8 -*-

#Exercise 2

#Task a.)

#inf means the positive infinity
#it occures while use to large numbers, e.g. 1e10000

# Task b.)
#variables of the type boolean can have the value True or False
# 3 != 3 gives the value False

#Task c.)

x = 0     #create variable x

print('Enter a number x = ')
input(x)    #create input
float(x)    #change string to float

y = 0
print('Enter a number y = ')
input(y)
float(y)    #same here

eps = 1e-15     #create very small variable

if (abs(x-y)<eps):      #comparing x-y to eps
    print('x == y')
else:
    print('x != y')