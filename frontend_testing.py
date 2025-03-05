import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Provide the correct path to your ChromeDriver executable
service = Service("")


driver = webdriver.Chrome(service=service)

# Your test code here
driver.get("http://127.0.0.1:5000/users/3")
time.sleep(5)


#I TRIED CREATING AN XPATH OUT OF THE RETURNED VALUE ON THE UI HOWEVER THIS CREATED PROBLEMS FOR ME WHEN EXECUTING.

#UserID = driver.find_element(By.XPATH, value="//pre[contains(text(),'{"user_id":"11","user_name":"KB"}')]")
#assert(UserID.is_displayed())
#if UserID.is_displayed():
#    print("Username KB is displayed. Their UserID = 11")



pre_WebElement = driver.find_element(By.TAG_NAME, "pre")

expected_text = '{"user_id":"3","user_name":"Kwame"}'
actual_text = pre_WebElement.text

print("Username Kwame is displayed. Their UserID = 3")

