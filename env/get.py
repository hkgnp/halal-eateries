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

# Total pages: 326
i=1
while i < 327:
    # Get page content
    print('Pushing Page: ' + str(i))
    results = driver.find_element_by_xpath('//*[@id="results"]/div')
    soup = BeautifulSoup(results.get_attribute('innerHTML'), 'html.parser')
    driver.implicitly_wait(10)
    output = soup.find_all("p")
    output_pretty = [{"name" : output[1], "add" : output[2]},{"name" : output[3], "add" : output[4]},{"name" : output[5], "add" : output[6]},{"name" : output[7], "add" : output[8]},{"name" : output[9], "add" : output[10]},{"name" : output[11], "add" : output[12]},{"name" : output[13], "add" : output[14]},{"name" : output[15], "add" : output[16]},{"name" : output[17], "add" : output[18]},{"name" : output[19], "add" : output[20]}]
    with open("halal-eateries.html", "a") as file:
        file.write(str(output_pretty))
    page = f"//*[@id='{i+1}']"
    driver.find_element_by_xpath(page).click()
    time.sleep(6)
    i+=1