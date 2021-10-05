from selenium import webdriver
import time
import calbot_data



driver = webdriver.Firefox()
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
        print("Pass - Google authorization in Firefox", file=file, sep="\n")
except:
    driver.save_screenshot("C:\\calbot\\Calbot screen\\Fail - Google authorization in Firefox.png")
    with open("Calbot test results.txt", "a") as file:
        print("Fail - Google authorization in Firefox.", file=file, sep="\n")

driver.quit() 
