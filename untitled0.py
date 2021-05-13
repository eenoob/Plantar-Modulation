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

#Increment hours run in a week by 2
for(int k='E2'; k<='E385')
{k=k+2};

#Increment weight by 2
for(int k='D2'; k<='D385')
{k=k+2};

#Decrement weight by 2
for(int k='D2'; k<='D385')
{k=k-2};

#Increment age by 2
for(int k='B2'; k<='B385')
{k=k+2};

#Decrement age by 2
for(int k='B2'; k<='B385')
{k=k-2};

#Swap genders
for(int k='C2'; k<='C385')
{if(k=0)
    k=1;
    else k=0;
    };


Combine all();

c11= data.groupby('INCOMEGRP4').size()
print c11

result = data.sort(['INCOMEGRP4'], ascending=[1])
print(result)
