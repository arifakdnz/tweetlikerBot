from selenium import webdriver
import logininfo
import time

browser = webdriver.Firefox(executable_path = "C:\\Users\\hp\\Desktop\\Selenium Python\\geckodriver.exe")

browser.get("https://twitter.com")

time.sleep(3)

first_login = browser.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div[1]/div/a[2]/div/span/span")
                                          
first_login.click()

time.sleep(2)


username = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input")
password = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input")

username.send_keys(logininfo.my_username)
password.send_keys(logininfo.my_password)

time.sleep(3)

login = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div/span/span")

login.click()

time.sleep(3)

searchArea = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")
searchArea.send_keys("fityemek")

time.sleep(2)

searchArea.send_keys(u'\ue007') #Enter button code

time.sleep(5)

i = 0
while i < 500:
    try:
    	    liker = browser.find_element_by_css_selector("[data-testid=like]")
    	    liker.click()
    	    i += 1
    except:
    	    pass 
browser.close()

