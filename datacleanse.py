# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 17:55:14 2020

@author: blapa
"""

import pandas as pd
import re

start = pd.Timestamp.now()
df = pd.read_csv('C:/Users/blapa/.spyder-py3/glassdoor/glassdoor_jobs.csv')
#Create a state column and sort by state
#remove rows where salary estimate is -1
#drop headquarters and competitors column
#find essential skills from job title 
#only selecting Salary Estimate = -1
df['hourly'] = df['Salary Estimate'].apply(lambda x:1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x:1 if 'employer provided salary:' in x.lower() else 0)

df = df[df['Salary Estimate'] != '-1']

#age of the company
df['age']= df['Founded'].apply(lambda x: x if x < 0 else 2020 - x)

#sas python aws spark rstudio sql tableau powerbi excel
df['python_yn']=df['Job Description'].apply(lambda x:'y' if 'python' in x.lower() else 'n')
df['sas_yn']=df['Job Description'].apply(lambda x:'y' if 'sas' in x.lower() else 'n')
df['aws_yn']=df['Job Description'].apply(lambda x:'y' if 'aws' in x.lower() else 'n')
df['spark_yn']=df['Job Description'].apply(lambda x:'y' if 'spark' in x.lower() else 'n')
df['rstudio_yn']=df['Job Description'].apply(lambda x:'y' if 'rstudio' in x.lower() else 'n')
df['sql_yn']=df['Job Description'].apply(lambda x:'y' if 'sql' in x.lower() else 'n')
df['tableau_yn']=df['Job Description'].apply(lambda x:'y' if 'tableau' in x.lower() else 'n')
df['xcel_yn']=df['Job Description'].apply(lambda x:'y' if 'excel' in x.lower() else 'n')
df['powerbi_yn']=df['Job Description'].apply(lambda x:'y' if 'powerbi' in x.lower() else 'n')

#dropping the columns with no values -1 in all rows 
new_df = df.drop(columns = ['Headquarters','Competitors'])
print(list(new_df.columns))
#Create a new state column
#new_df['State']=new_df['Location'].str[-2:]
new_df['State']=new_df['Location'].apply(lambda x:x.split(',')[-1])
#new_df['Location']=new_df['Location'].apply(lambda x:x.split(',')[0])
#new_df['Salary Estimate']=new_df['Salary Estimate'].apply(lambda x:x.replace("(Glassdoor Est.)",'').replace('$','').replace('K',''))
new_df['Salary Estimate']=new_df['Salary Estimate'].apply(lambda row: re.sub("[^0-9-]", "", row))

new_df['min_salary']=new_df['Salary Estimate'].apply(lambda x:x.split('-')[0])
new_df['max_salary']=new_df['Salary Estimate'].apply(lambda x:x.split('-')[1])
#removing the rating from Company Name
new_df['Company']=new_df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3],axis=1)
#(new_df.State.value_counts())
new_df.to_csv("gd-Salary-cleaned.csv",index=False)
print(pd.Timestamp.now()-start) 
