#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 14:11:21 2020

@author: nick
"""

import numpy as np
import pandas as pd

#make cars dictionary
cars={'make':['Ford','GM','Toyota','Nissan'],
      'model':['Mustang','Spitfire','Yarris','Sentra'],
      'doors':[2,2,4,2],
      'price':[12000,34000,26000,18000]}
print(cars)
print('\n')

#load from dictionary
df=pd.DataFrame(cars)
print(df)
print('\n')

#load dataframe from csv file
df=pd.read_csv('cars.csv')
print(df)
print('\n')

print(df[0:2])
print(df[2:3])
print(df[-1:])
print('\n')

#reverse dataframe
print(df[::-1])
print('\n')

#Accessing individual columns
#df['column_name']
#data is returned as a series of values rather than a dataframe
#to return dataframe, use double square brackets
#df[['column_name]]

print(df['Make'])
print('\n')

#return a dataframe just with the make column
print(df[['Make']])
print('\n')

#data frame with make and model
print(df[['Make','Model']])
print('\n')

#loc and iloc - loc uses labels, iloc uses integers
#[start_index:end_index] - data returned as data frame
#[start_index,end_index] - data is returned as a series of values

#return data row 0 as a series
print(df.iloc[0])
print('\n')

#return data row 0 as data frame
print(df.iloc[[0]])
print('\n')

#select make and model columns
print(df.iloc[:,0:2])
print('\n')

#return make and model columns and row 1&2 as a data frame
print(df.iloc[1:3,0:2])
print('\n')

#use loc to specify columns returned as data frame
print(df.loc[:,['Model','Make','Doors']])
print('\n')

#To use loc for specifying rows, we need to make an index column
#then look for row
#set 'Make' column as index
df.set_index('Make',inplace=True)
print(df)
print('\n')

#locate Ford row - use single [] for series, [[]] for data frame
print(df.loc['Ford'])
print(df.loc[['Ford']])
print('\n')

#locate Ford and GM row with Model and Price
print(df.loc['Ford':'GM',['Model','Price']])

#reload dataframe to restore integer index
df=pd.read_csv('cars.csv')
#df=pd.DataFrame(cars)
#print(df.loc[df['Make']=='Ford']) - not working
#print(df.loc[df['Make'].isin(['Ford','GM']),['Model','Price']]) - not working

#Add row to data frame
car={'Make':'BMW',
     'Model':'Rover',
     'Doors':2,
     'Price':24000}

#Append car to dataframe
df=df.append(car,ignore_index=True)
print(df)



print('\n')