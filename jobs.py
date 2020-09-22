# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 23:00:48 2020

@author: blapa
"""

import glassdoor_scraper as gs 
import pandas as pd 

path = "C:/Users/blapa/Downloads/chromedriver_win32/chromedriver.exe"

df = gs.get_jobs('data scientist',10, False, path, 5)

#df.to_csv('glassdoor_jobs.csv', index = False)

