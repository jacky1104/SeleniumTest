from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# browser = webdriver.Chrome("C:\Users\jacky\AppData\Local\Programs\Python\Python36\chromedriver") # Get local session of firefox
browser = webdriver.Chrome() # Get local session of firefox
# browser = webdriver.Chrome("C:\Users\jacky\AppData\\Local\\Programs\\Python\\Python36\\chromedriver") # Get local session of firefox
browser.get("http://192.168.1.99/login") # Load page
# assert "172.16.95.57!" in browser.title
elem = browser.find_element_by_id("username") # Find the query box
elem.send_keys("admin" + Keys.RETURN)
time.sleep(3) # Let the page load, will be added to the API
# elemPassword = browser.find_element_by_id("secretkey") # Find the query box
# elemPassword.send_keys("" + Keys.RETURN)
# browser.find_element_by_id("login_button").click()

laterButton = browser.find_element_by_xpath('//*[@id="navbar-view-section"]/div/f-forticare-license-prompt/div/div/div[2]/span/div[2]/button[2]')
laterButton.click()
time.sleep(2)


fortiview = browser.find_element_by_xpath('.//*[@id="navbar-view-section"]/nav/ul/li[3]/div[2]/div/span[1]')
fortiview.click()
time.sleep(3)


flag=True

for i in range(500):
    source = browser.find_element_by_xpath('.//*[@id="navbar-view-section"]/nav/ul/li[3]/div[2]/f-navbar-menu/ul/li[1]/div[2]/f-navbar-menu/ul/li[1]/div/a/span')
    source.click()
    time.sleep(1)
    destination = browser.find_element_by_xpath('.//*[@id="navbar-view-section"]/nav/ul/li[3]/div[2]/f-navbar-menu/ul/li[1]/div[2]/f-navbar-menu/ul/li[2]/div/a/span')
    destination.click()
    if (flag):
        nowButton = browser.find_element_by_xpath(
            '//*[@id="navbar-view-section"]/div/div/div/div[1]/div[3]/div[2]/div/button')
        nowButton.click()
        flag = False
        hourButton = browser.find_element_by_xpath('/html/body/div[9]/div[3]/button/div/span')
        hourButton.click()
        time.sleep(1)

print("so easy selenium web test")
# try:
#     browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
# except NoSuchElementException:
#     assert 0, "can't find seleniumhq"
# browser.close()