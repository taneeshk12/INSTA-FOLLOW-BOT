from selenium import webdriver
from time import sleep
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://instagram.com")
sleep(4)
driver.find_element_by_xpath(("//input[@name=\"username\"]"))\
    .send_keys(("your username"))
driver.find_element_by_xpath(("//input[@name=\"password\"]"))\
    .send_keys(("your password"))    
driver.find_element_by_xpath('//button[@type="submit"]')\
    .click()
sleep(3) 
for i in range(7):
    #enter link of profile you want to follow their followers
    driver.get("https://www.instagram.com/akshaykumar/")
    sleep(5)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')\
        .click()
    sleep(2)    
    #follow users up to the specified height
    follow=driver.find_elements_by_xpath("/html/body/div[4]/div/div[2]/ul/div/li[1]/div/div[3]/button")
    for x in range (0,len(follow)):
        follow[x].click()
        sleep(2)

    # Get all buttons that has the text Follow 
    for i in range(5):
        buttons = driver.find_elements_by_xpath("//button[contains(.,'Follow')]")
        for btn in buttons:
            if btn.text == 'Follow': 
                driver.execute_script("arguments[0].click();", btn)
                sleep(10)
        driver.refresh()    
sleep(24*3600)        
          
        
        
    

