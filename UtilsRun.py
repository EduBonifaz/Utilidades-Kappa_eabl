from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
from Code.DCDQRules import DCQRRulesGen
from Code.RCRules import RCRulesGen
import re
import os

CHROMEDRIVER_PATH = r""   #/chromedriver_win32/chromedriver.exe

options = webdriver.ChromeOptions()
options.add_argument(r'--user-data-dir=C:/Users/user/AppData/Local/Google/Chrome/User Data')
options.add_argument(r'--profile-directory=Profile 1') # Colocar su Profile
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)

paths = [
]

driver.get('https://www.google.com')

pathconfs = []
for path in paths:
    driver.get(path.replace("/browse/","/raw/"))
    try:
        WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH,'/html/body/pre')))
        time.sleep(0.2)
        ConfText = driver.find_element(By.XPATH,'/html/body/pre').text
    except:
        print("Fallo")
    pathconfs.append(ConfText)

ListVar=[]

for pathconf in pathconfs:
    Variables=re.findall(r"(?<=\$\{)[\?A-Z0-9_]+(?=\})",pathconf)
    Variables = list(set(Variables))
    ListVar.extend(Variables)
ListVar = list(set(ListVar))
for data in ListVar:
    if '?' in data:
        data=data.replace('?','')
        os.environ[data] = '"${?'+data+'}"'
    else:
        os.environ[data] = '"${'+data+'}"'

spreedsheetRC = ""
RCRulesGen(pathconfs, spreedsheetRC)

spreedsheetDCQR = ""
DCQRRulesGen(pathconfs, spreedsheetDCQR)