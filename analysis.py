# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 10:02:53 2018

@author: caren
"""
#importing the package pandas and call it pd then use pd to read in the data

import pandas as pd
oceania = pd.read_csv('data/gapminder_gdp_oceania.csv', index_col = 'country')

#working with oceania data