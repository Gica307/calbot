from selenium import webdriver
import calbot_data



driver = webdriver.Firefox()
try:     
    driver.get('https://app.calbot.co.uk')
    driver.find_element_by_xpath(calbot_data.authorization_microsoft).click()    
    driver.find_element_by_xpath(calbot_data.authorization_exchange).click()        
    driver.find_element_by_name(calbot_data.exchangeInputMail).send_keys(calbot_data.mail_exchange)
    driver.find_element_by_name(calbot_data.exchangeInputPassword).send_keys(calbot_data.password_exchange)
    driver.find_element_by_xpath(calbot_data.exchangeMailPasswordNext).click()   
    with open("Calbot test results.txt", "a") as file:
        print("Pass - Exchange authorization in Firefox", file=file, sep="\n")
except:
    driver.save_screenshot("C:\\calbot\\Calbot screen\\Fail - Exchange authorization in Firefox.png")
    with open("Calbot test results.txt", "a") as file:
        print("Fail - Exchange authorization in Firefox.", file=file, sep="\n")

driver.quit() 