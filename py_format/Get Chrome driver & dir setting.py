#!/usr/bin/env python
# coding: utf-8

# # Get Chrome Driver

# In[1]:


get_ipython().run_line_magic('pwd', '#check current directory')


# In[2]:


## Create directory 
get_ipython().run_line_magic('cd', 'c:/')
get_ipython().system('mkdir chrome_webdriver')
get_ipython().run_line_magic('cd', 'c:chrome_webdriver')


# In[3]:


## Insatll wget package & import module
get_ipython().system('pip install wget')
import wget


# In[5]:


## Get Chrome driver
"""Check out your Chrome Driver version and get equivalent driver of version.
If you don't know your chrome version, please refer to the url below.
https://help.zenplanner.com/hc/en-us/articles/204253654-How-to-Find-Your-Internet-Browser-Version-Number-Google-Chrome
'~win32.zip' is available in both win64 & win32.
Delete remark and download"""

# wget.download("https://chromedriver.storage.googleapis.com/91.0.4472.19/chromedriver_win32.zip")  #91
# wget.download('https://chromedriver.storage.googleapis.com/90.0.4430.24/chromedriver_win32.zip')  #90   
# wget.download("https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_win32.zip")  #89
# wget.download("https://chromedriver.storage.googleapis.com/88.0.4324.96/chromedriver_win32.zip")  #88
# wget.download("https://chromedriver.storage.googleapis.com/87.0.4280.88/chromedriver_win32.zip")  #87
# wget.download("https://chromedriver.storage.googleapis.com/86.0.4240.22/chromedriver_win32.zip")  #86
# wget.download("https://chromedriver.storage.googleapis.com/85.0.4183.87/chromedriver_win32.zip")  #85


# In[6]:


import zipfile
temp1 = zipfile.ZipFile("c:\\chrome_webdriver\\chromedriver_win32.zip")
temp1.extractall('c:\\chrome_webdriver')
temp1.close()


# # Set Directory 
# (save path)

# In[11]:


get_ipython().run_line_magic('cd', 'd:/  # if you wanna change dir, just change d >> c or something else')


# In[13]:


get_ipython().system('mkdir images')
get_ipython().system('mkdir images\\\\bing')
get_ipython().system('mkdir images\\\\google')
get_ipython().system('mkdir images\\\\instagram')
get_ipython().system('mkdir images\\\\naver')
get_ipython().system('mkdir images\\\\pinterest')

