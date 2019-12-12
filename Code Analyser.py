# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:21:16 2019

@author: 761317
"""
import re
import PythonVariableClassifier as PVC

variables=[]
finalvariables=[]

functions=[]

def findVariables(line,variables):
     x = re.search(r"\b=\w+", line)
     if x is not None:
       lineeq=x.string
   
       lineeqlist=lineeq.split("=")
       
       if lineeqlist[0] not in variables:
           if(lineeqlist[0].count(',')>0):
               
               
               splitter=lineeqlist[0].split(',')
               for var in splitter:
                   variables.append(var.replace(" ",""))
                   
           else:
               variables.append(lineeqlist[0].replace(" ",""))
               
               
               
def variableUsage():
    pass
    
    
    
def functionAnalyser():
    pass
        
    
    
    
    

    
               

def findFunctions(line,functions):
     
     if line.count("(") > 0:
         m = re.search('def(.+?)\)', line)
         
         if m is not None:
             linefu=m.group()
             linefu=linefu.replace(" ","")
             fu = re.search('def(.+?)\(', linefu)
             fu=fu.group().replace("def","")
             fu=fu.replace("(","")
             functions.append(fu)


     

import nltk   
fp = open('TrendPlotter.py', 'rU')

for line in fp:
   findVariables(line,variables)
   findFunctions(line,functions)
   raw=fp.read()
   tokens = nltk.word_tokenize(raw)
   text = nltk.Text(tokens)
for var in variables:
    
         if(PVC.pythonVariableClassifier(var)==1):
             finalvariables.append(var)
             
             
print("The Variables in the given Program")
i=1
for var in finalvariables:
    print(i,end=". ")
    print(var)
    i+=1
print("The functions defined in the given program are")
i=1
for function in functions:
    print(i,end=". ")
    print(function)
    i+=1



