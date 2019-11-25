#!/usr/bin/env python
# coding: utf-8

# In[13]:


#下載指定檔案到 Data 資料夾，存成檔名 Homework.txt
from urllib.request import urlretrieve
import os

try:
    os.makedirs( './Data', exist_ok=True )
    
    urlretrieve ("https://www.w3.org/TR/PNG/iso_8859-1.txt", "./data/Homework.txt")
    
except:
    print('發生錯誤！')


# In[16]:


#檢查 Data 資料夾是否有 Homework.txt 檔名之檔案
files = []

import os, sys

dirs = os.listdir( './data' )

for files in dirs:
    print(files)

if 'Homework.txt' in files:
    print('[O] 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案')
else:
    print('[X] 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案')


# In[25]:


#將「Hello World」字串覆寫到 Homework.txt 檔案

with open ("./Data/Homework.txt","w") as h:
    h.write("Hello World")


# In[29]:


# 檢查 Homework.txt 檔案字數是否符合 Hello World 字數

import chardet
 
f = open("./Data/Homework.txt", "rb")
data = f.read()

if len("Hello World") == len(data):
    print('[O] 檢查 Homework.txt 檔案字數是否符合 Hello World 字數')
else:
    print('[X] 檢查 Homework.txt 檔案字數是否符合 Hello World 字數')
    


# In[ ]:




