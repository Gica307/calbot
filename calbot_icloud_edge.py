from selenium import webdriver
import calbot_data
import time



driver = webdriver.Edge('C:\\calbot\\msedgedriver.exe')
try: 
    driver.get('https://app.calbot.co.uk')
    driver.find_element_by_xpath(calbot_data.authorization_icloud).click()
    time.sleep(2)
    main_window = driver.window_handles[0]
    new_window = driver.window_handles[1]
    driver.switch_to_window(new_window)
    time.sleep(1)
    driver.find_element_by_id(calbot_data.icloudInputMail).send_keys(calbot_data.mail_icloud)    
    time.sleep(1)
    driver.find_element_by_id(calbot_data.icloudInputPassword).send_keys(calbot_data.password_icloud)
    driver.find_element_by_id(calbot_data.icloudchecbox).click()
    driver.find_element_by_xpath(calbot_data.icloudMailPasswordNext).click()
    driver.switch_to_window(main_window)
    with open("Calbot test results.txt", "a") as file:
        print("Pass - iCloud authorization in Edge", file=file, sep="\n")
except:
    driver.save_screenshot("C:\\calbot\\Calbot screen\\Fail - iCloud authorization in Edge.png")
    with open("Calbot test results.txt", "a") as file:
        print("Fail - iCloud authorization in Edge.", file=file, sep="\n")

driver.quit()