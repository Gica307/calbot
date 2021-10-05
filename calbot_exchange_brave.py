from selenium import webdriver
import calbot_data



driver_path = "C:\\calbot\\chromedriver.exe"
brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
option = webdriver.ChromeOptions()
option.binary_location = brave_path
driver = webdriver.Chrome(executable_path=driver_path, options=option)

try:    
    driver.get('https://app.calbot.co.uk')
    driver.find_element_by_xpath(calbot_data.authorization_microsoft).click()    
    driver.find_element_by_xpath(calbot_data.authorization_exchange).click()        
    driver.find_element_by_name(calbot_data.exchangeInputMail).send_keys(calbot_data.mail_exchange)
    driver.find_element_by_name(calbot_data.exchangeInputPassword).send_keys(calbot_data.password_exchange)
    driver.find_element_by_xpath(calbot_data.exchangeMailPasswordNext).click()   
    with open("Calbot test results.txt", "a") as file:
        print("Pass - Exchange authorization in brave", file=file, sep="\n")
except:
    driver.save_screenshot("C:\\calbot\\Calbot screen\\Fail - Exchange authorization in brave.png")
    with open("Calbot test results.txt", "a") as file:
        print("Fail - Exchange authorization in brave.", file=file, sep="\n")

driver.quit() 