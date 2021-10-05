from selenium import webdriver
import time
import calbot_data



driver_path = "C:\\calbot\\chromedriver.exe"
brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
option = webdriver.ChromeOptions()
option.binary_location = brave_path
driver = webdriver.Chrome(executable_path=driver_path, options=option)

try:    
    driver.get('https://app.calbot.co.uk')
    driver.find_element_by_xpath(calbot_data.authorization_google).click()
    time.sleep(1)
    main_window = driver.window_handles[0]
    new_window = driver.window_handles[1]
    driver.switch_to_window(new_window)
    time.sleep(1)
    driver.find_element_by_id(calbot_data.googleInputMail).send_keys(calbot_data.mail_google)
    driver.find_element_by_id(calbot_data.googleMailNext).click()
    time.sleep(1)
    driver.find_element_by_id(calbot_data.googleInputPassword).send_keys(calbot_data.password_google)
    driver.find_element_by_id(calbot_data.googlePasswordNext).click()
    driver.switch_to_window(main_window)
    with open("Calbot test results.txt", "a") as file:
        print("Pass - Google authorization in brave", file=file, sep="\n")
except:
    driver.save_screenshot("C:\\calbot\\Calbot screen\\Fail - Google authorization in brave.png")
    with open("Calbot test results.txt", "a") as file:
        print("Fail - Google authorization in brave.", file=file, sep="\n")

driver.quit() 
