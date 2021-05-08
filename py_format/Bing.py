#!/usr/bin/env python
# coding: utf-8

# ### Bing

# In[1]:


### Bing
"""Before execute code below, check out your kernel or jupyter notebook kernel environment 
If you have problem, just copy this code and paste to yout jupyter notebook (recommended)
Also, before execute this page, execute this first >> "Get Chrome driver & dir setting.ipynb"

browser must be pop up on the screen : if the browser is in a state of minimization, results may go bad
(It does not matter covering the page with other page like jupyternotebook >> you can do other works)

If you have trouble with lxml, selenium, bs4, try to isntall module in anaconda prompt
>>> execute anconda prompt, try to [conda install lxml], [conda install selenium], [conda install bs4]

warning : If you try this code with high frequency, Search engine may ban your ip temporarily (for 5~10 minutes)

Refer to : Scroll_cnt=5 >>> about 100~200 imgs (depending on the searching word)"""


## Install module required
#!pip install lxml
#!pip install selenium
#!pip install bs4


## Import modules
import urllib.request    
from bs4 import BeautifulSoup    
from selenium import webdriver    
from selenium.webdriver.common.keys import Keys
import time    


##### Path ######################################################################
Chromedriver_PATH = 'c:\\chrome_webdriver\\chromedriver.exe'  # Chromedriver PATH 
save_path = 'd:\\images\\bing\\'  #save_path 
#################################################################################


## get userdata & parameters
Search_Tag = input("Input Search_Tag : ")  # Search_Tag
scroll_cnt = int(input("Input scroll_cnt : "))  #scroll count
scrolltime = float(input("Input scroll_sleep_second >>> range(5~10) : "))  #Sleep time 


## Get driver & open
driver = webdriver.Chrome(Chromedriver_PATH)  # Chromedriver PATH 
driver.get("https://www.bing.com/images?Form=Z9LH")    
driver.maximize_window()
time.sleep(1)


## input Search_Tag & Submit
elem = driver.find_element_by_id("sb_form_q")    
elem.send_keys(Search_Tag)
time.sleep(1.5)  #Do not remove >> if you remove this line, can't go next step 
elem.submit()
time.sleep(3.0)  #Do not remove


############## Functions ################################################################################
def fetch_list_url():  #parsing src url
    imgList = soup.find_all("img", class_="mimg")
    for im in imgList:
        params.append(im["src"])  
    return params


def fetch_detail_url():  #save src to local  #changing save_path : Go to the top of this page (Path)
    for idx,p in enumerate(params,1):  #enumerate idx option 1 : get start index from 1 (default=0)
        urllib.request.urlretrieve(p, save_path + Search_Tag + '_' + str(idx) + "_bing" + ".jpg")
###########################################################################################################    


## Scrolling & Parsing
params=[]
for i in range(scroll_cnt):
    html = driver.page_source  #get source         
    soup = BeautifulSoup(html, "lxml") 
    params = fetch_list_url()  #save the img_url to params
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  #scroll
    time.sleep(scrolltime)


## Save imgs
print('')
print("Overlaped srcs : ", len(params))
params=list(dict.fromkeys(params))  #delete overlap  #index URL >> https://m31phy.tistory.com/130
fetch_detail_url()  #save img
print("Non_Overlap srcs : ", len(params))


driver.close()  #close browser

