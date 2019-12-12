# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:40:58 2019

@author: 761317

import difflib
text1 = open("AllAnalyser.py").readlines()
text2 = open("Analyser.py").readlines()

for line in difflib.unified_diff(text1, text2):
    print(line)
"""
import requests
import tkinter
print(requests.__version__)