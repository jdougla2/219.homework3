# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 21:20:06 2019

@author: Beezlebub
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import scipy.stats

with open("meteorites.json", "r", encoding="utf8") as read_file:
    data = json.load(read_file)
    del data[12]
    meates = pd.DataFrame.from_dict(data)
years = meates['year']
#del years[12]
thing = years[0]
thing = thing[:4]
years2 = []
for x in years:
    thingy = str(x)[:4]
    years2.append(thingy)
mass = meates['mass']
#mass[12]
massLbs = []
for x in mass:  
    boyo = float(x) * 2.205         
    massLbs.append(boyo)
mass2 = pd.DataFrame(massLbs, columns=['mass'])
years3 = pd.DataFrame(years2, columns=['year'])
halves = [years3, mass2]
combined = pd.concat(halves, axis=1)

year3 = years3.sort_values(by=['year'])
yearCount = years3['year'].value_counts()
#x_vals