from selenium import webdriver
import time
import calbot_data


driver = webdriver.Firefox()
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
    time.sleep(1)
    driver.find_element_by_id(calbot_data.outlookInputPassword).send_keys(calbot_data.password_outlook)
    driver.find_element_by_id(calbot_data.outlookPasswordNext).click()
    driver.find_element_by_id(calbot_data.outlookPasswordNext).click()
    driver.switch_to_window(main_window)
    with open("Calbot test results.txt", "a") as file:
        print("Pass - Outlook authorization in google chrome", file=file, sep="\n")
except:
    driver.save_screenshot("C:\\calbot\\Calbot screen\\Fail - Outlook authorization in Firefox.png")
    with open("Calbot test results.txt", "a") as file:
        print("Fail - Outlook authorization in Firefox.", file=file, sep="\n")

driver.quit() 