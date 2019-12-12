# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 10:32:21 2019

@author: 761317
"""

import pandas as pd
import re
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import train_test_split
data=pd.read_csv("PythonVariables.csv")
data.head()
x=data[["Length","StartsWithAlpha","ContainsSymbols"]]
y=data[["IsVariable"]]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.01,random_state=1)
from sklearn.tree import DecisionTreeClassifier  
clf = DecisionTreeClassifier(max_depth=5)
clf = clf.fit(x_train,y_train)
alpha="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
def pythonVariableClassifier(str1):
    length=len(str1)
    StartsWithAlpha=0
    if str1[0] in alpha:
        StartsWithAlpha=1
    else:
        StartsWithAlpha=0
    verify = re.compile('[@!#$%^&*()<>?/\|}{~:]')
    ContainsSymbols=1
    if(verify.search(str1) == None): 
       ContainsSymbols=0
          
    else: 
        ContainsSymbols=1
    return clf.predict([[length,StartsWithAlpha,ContainsSymbols]])   
       
