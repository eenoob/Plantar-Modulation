# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 14:06:38 2021

@author: Abhijit
"""

import pandas
import numpy
import seaborn

data = pandas.read_csv('dataset.csv', low_memory=False)

#Set PANDAS to show all columns in DataFrame
pandas.set_option('display.max_columns', None)
#Set PANDAS to show all rows in DataFrame
pandas.set_option('display.max_rows', None)

# bug fix for display formats to avoid run time errors
pandas.set_option('display.float_format', lambda x:'%f'%x)

#setting variables you will be working with to numeric
data['WEIGHT'] = data['WEIGHT'].convert_objects(convert_numeric=True)
data['HOURS'] = data['HOURS'].convert_objects(convert_numeric=True)
data['AGE'] = data['AGE'].convert_objects(convert_numeric=True)
data['SEX'] = data['SEX'].convert_objects(convert_numeric=True)

pointer(random) = NULL
k -> col

# Picking up random 55 entries from 1 to 385 
for(int k='1'; k<='385')
random(55)
Arr1[]=random(55)
set pointer->default;

# Picking up random 55 entries from 386 to 769 
for(int k='386'; k<='769')
random(55)
Arr1[]=random(55)
set pointer->default;

# Picking up random 55 entries from 770 to 1153 
for(int k='770'; k<='1153')
random(55)
Arr1[]=random(55)
set pointer->default;

# Picking up random 55 entries from 1154 to 1537 
for(int k='1154'; k<='1537')
random(55)
Arr1[]=random(55)
set pointer->default;

# Picking up random 55 entries from 1538 to 1921 
for(int k='1538'; k<='1921')
random(55)
Arr1[]=random(55)
set pointer->default;

# Picking up random 55 entries from 1922 to 2305 
for(int k='1922'; k<='2305')
random(55)
Arr1[]=random(55)
set pointer->default;

# Picking up random 55 entries from 2306 to 2689 
for(int k='2306'; k<='2689')
random(55)
Arr1[]=random(55)
set pointer->default;

Combine all();

c11= data.groupby('INCOMEGRP4').size()
print c11

result = data.sort(['INCOMEGRP4'], ascending=[1])
print(result)
