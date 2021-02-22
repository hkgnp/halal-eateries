# import required modules 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

import time 

# create instance of Chrome webdriver
options = Options()
options.headless = True;
driver = webdriver.Chrome(options = options) 
driver.get("https://www.muis.gov.sg/Halal/Halal-Certification/Certified-Eating-Establishments#") 

driver.implicitly_wait(10)

# enter asterisk 
driver.find_element_by_xpath('//*[@id="txtHalalSearch"]').send_keys('*') 

# click on Search 
driver.find_element_by_xpath( 
	'//*[@id="btnHalalSearch"]').click() 

i=1
while i < 2:
    # Get page content
    print(i)
    results = driver.find_element_by_xpath('//*[@id="results"]/div')
    soup = BeautifulSoup(results.get_attribute('innerHTML'), 'html.parser')
    driver.implicitly_wait(10)
    output = soup.find_all("p")
    with open("halal-eateries.html", "a") as file:
        file.write(str(output))
    page = f"//*[@id='{i+1}']"
    driver.find_element_by_xpath(page).click()
    time.sleep(6)
    i+=1