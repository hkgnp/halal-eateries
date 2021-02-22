# import required modules 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

import time 

# create instance of Chrome webdriver
options = Options()
options.headless = False
driver = webdriver.Chrome(options = options) 
driver.get("https://www.muis.gov.sg/Halal/Halal-Certification/Certified-Eating-Establishments#") 

driver.implicitly_wait(100)

# enter asterisk 
driver.find_element_by_xpath('//*[@id="txtHalalSearch"]').send_keys('*') 

# click on Search 
driver.find_element_by_xpath( 
	'//*[@id="btnHalalSearch"]').click() 

# Wait 200ms
# driver.implicitly_wait(8000)

i=1
while i < 3:
    # Get page content
    driver.implicitly_wait(20000)
    results = driver.find_element_by_class_name('search-result')
    soup = BeautifulSoup(results.get_attribute('innerHTML'), 'html.parser')
    output = soup.find_all("p")
    with open("output1.html", "a") as file:
        file.write(str(output))
    page = f"//*[@id='{i+1}']"
    driver.find_element_by_xpath(page).click()
    i+=1
    