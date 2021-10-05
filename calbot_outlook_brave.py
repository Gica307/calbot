from selenium import webdriver
import calbot_data
import time



driver_path = "C:\\calbot\\chromedriver.exe"
brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
option = webdriver.ChromeOptions()
option.binary_location = brave_path
driver = webdriver.Chrome(executable_path=driver_path, options=option)

try:    
    driver.get('https://app.calbot.co.uk')
    driver.find_element_by_xpath(calbot_data.authorization_microsoft).click()
    time.sleep(1)
    driver.find_element_by_xpath(calbot_data.authorization_outlook).click()
    time.sleep(2)
    main_window = driver.window_handles[0]
    new_window = driver.window_handles[1]
    driver.switch_to_window(new_window)
    time.sleep(1)
    driver.find_element_by_id(calbot_data.outlookInputMail).send_keys(calbot_data.mail_outlook)
    driver.find_element_by_id(calbot_data.outlookMailNext).click()
    time.sleep(2)
    driver.find_element_by_id(calbot_data.outlookInputPassword).send_keys(calbot_data.password_outlook)
    driver.find_element_by_id(calbot_data.outlookPasswordNext).click()
    driver.find_element_by_id(calbot_data.outlookPasswordNext).click()
    driver.switch_to_window(main_window)
    with open("Calbot test results.txt", "a") as file:
        print("Pass - Outlook authorization in brave", file=file, sep="\n")
except:
    driver.save_screenshot("C:\\calbot\\Calbot screen\\Fail - Outlook authorization in brave.png")
    with open("Calbot test results.txt", "a") as file:
        print("Fail - Outlook authorization in brave.", file=file, sep="\n")

driver.quit() 