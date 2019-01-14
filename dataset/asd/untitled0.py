#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:08:38 2019

@author: alperen
"""
import pandas as pd
x=pd.read_csv("input.data")

x['Open']=x['Open'].round().fillna(0.0).astype(int)
x['High']=x['High'].round().fillna(0.0).astype(int)
x['Low']=x['Low'].round().fillna(0.0).astype(int)
x['Close']=x['Close'].round().fillna(0.0).astype(int)
x['Adj Close']=x['Adj Close'].round().fillna(0.0).astype(int)
x.to_csv('iris.data')
print(x)
print(x.dtypes)