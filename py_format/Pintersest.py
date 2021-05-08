#!/usr/bin/env python
# coding: utf-8

# ### Pinterest

# In[1]:


### Pinterest scrolling 

"""Before execute code below, check out your kernel or jupyter notebook kernel environment 
If you have problem, just copy this code and paste to yout jupyter notebook (recommended)
Also, before execute this page, execute this first >> "Get Chrome driver & dir setting.ipynb"

You must login with Pinterest Account ---> You Can't login with google account.
I try to login with google, i don't have solution with new browser pop up issue.
And browser must be pop up on the screen : if the browser is in a state of minimization, results may go bad
(It does not matter covering the pinterest page with other page like jupyternotebook >> you can do other works)

If you have trouble with lxml, selenium, bs4, try to isntall module in anaconda prompt
>>> execute anconda prompt, try to [conda install lxml], [conda install selenium], [conda install bs4]

warning : If you try this code with high frequency, Search engine may ban your ip temporarily (for 5~10 minutes)

Refer to : Scroll_cnt=5 >>> about 307 imgs(depending on the searching word)"""


## Install module required
# !pip install lxml
# !pip install selenium
# !pip install bs4


## Import modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import urllib.request
from time import sleep
import time as time
import getpass


##### Path ######################################################################
Chromedriver_PATH = 'c:\\chrome_webdriver\\chromedriver.exe'  # Chromedriver PATH 
save_path = 'D:\\images\\pinterest\\'  #save_path 
#################################################################################


## get userdata & parameters
username = input("Input ID : ")  # User ID
password = getpass.getpass("Input PWD : ")  # User PWD  #getpass : hidden option
Search_Tag = input("Input Search_Tag : ")  # Search_Tag
scroll_cnt = int(input("Input scroll_cnt : "))  #scroll count
scrolltime = float(input("Input scroll_sleep_second >>> range(5~10) : "))  #Sleep time 


## Get driver & open
driver = webdriver.Chrome(Chromedriver_PATH)  # Chromedriver PATH 
driver.get("https://www.pinterest.co.kr/")
driver.maximize_window()
sleep(1)


## click login botton
driver.find_element_by_css_selector(".RCK.Hsu.USg.adn.CCY.czT.Vxj.aZc.Zr3.hA-.Il7.Jrn.hNT.BG7.gn8.L4E.kVc").click()


# ## login with goggle : Preparing...
# driver.find_element_by_css_selector(".S9gUrf-YoZ4jf").click()


### Login with Pinterest account
# insert logindata in "login div"
element_id = driver.find_element_by_name("id")
element_id.send_keys(username)
element_password = driver.find_element_by_name("password")
element_password.send_keys(password) 
driver.implicitly_wait(1)

## click login botton : by Pinterest account
driver.find_element_by_css_selector('.red.SignupButton.active').click()

## input Search_Tag & push 'Enter'
time.sleep(10)  #recommand not to change times
driver.page_source  #get source         

search = driver.find_element_by_name("searchBoxInput")
search.send_keys(Search_Tag)

time.sleep(5)  #recommand not to change times
search.send_keys(Keys.ENTER)
time.sleep(5)  #recommand not to change times


############## Functions ################################################################################
def fetch_list_url():  #parsing src url
    imgList = soup.find_all("img", class_="hCL kVc L4E MIw")
    for im in imgList:
        try :
            params.append(im["src"])  
        except KeyError:
            params.append(im["srcset"])
    return params
    
def fetch_detail_url():  #save src to local  #changing save_path : Go to the top of this page (Path)
    for idx,p in enumerate(params,1):  #enumerate idx option 1 : get start index from 1 (default=0)
        urllib.request.urlretrieve(p, save_path + Search_Tag + '_' + str(idx) + ".jpg")
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

