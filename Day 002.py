#!/usr/bin/env python
# coding: utf-8

# In[1]:


#下載指定檔案到 Data 資料夾，存成檔名 Homework.txt
from urllib.request import urlretrieve
import os

try:
        
    urlretrieve ("http://pycrawler.cupoy.com/file-download/part02/example.csv", "day02.csv")
    
except:
    print('發生錯誤！')


# In[31]:


import csv

with open('day02.csv',encoding = 'utf8', newline='') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        print(row)


# In[50]:


import csv

with open('day02.csv',encoding = 'utf8', newline='') as csvfile:
    rows = csv.reader(csvfile)
    headers = next(rows)
    for row in rows:
        if header:
            first = row.index('班次1')
            header = not header
            continue
        
        print(row[first])


# In[54]:


data = []

import csv

with open('day02.csv',encoding = 'utf8', newline='') as csvfile:
    rows = csv.reader(csvfile)
    headers = next(rows)
    for row in rows:
        data.append(row[5])
print(data)


# In[47]:


# 3. 將班次一到五與其所有時間用一種資料型態個別保存
import csv

with open('day02.csv',encoding = 'utf8', newline='') as csvfile:
    rows = csv.reader(csvfile)
    columns = ['班次1', '班次2', '班次3', '班次4', '班次5']
    column_idxs = []
    shifts = {col:list() for col in columns}
    header = True
    for row in rows:
        if header:
            for idx, col in enumerate(columns):
                column_idxs.insert(idx, row.index(col))
                header = not header
                continue
        
        for idx, col in enumerate(columns):
            shifts[col].append(row[column_idxs[idx]])
print(shifts)


# In[ ]:




