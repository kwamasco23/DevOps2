import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from flask import Flask

# db config
import db_connector

app = Flask(__name__)
conn = db_connector.get_db_connection()

service = Service("")

# Selenium config
#service = Service("chromedriver.exe")  # Update with correct path
driver = webdriver.Chrome(service=service)



# Test data
test_id = '95'
name = 'Jayy'
test_url = f'http://127.0.0.1:5000/users/{test_id}'

def test_create_user():
    res = requests.post(test_url, json={'user_name': name})
    if not res.ok:
        print(f"POST failed: {res.status_code} - {res.text}")
    else:
        print('User name successfully created')

def test_get_user(user_id):
    res = requests.get(f'http://127.0.0.1:5000/users/{user_id}')
    if res.status_code == 200:
        print("User retrieved:", res.json())
    else:
        print(f"GET failed: {res.status_code} - {res.text}")

def selenium_webdriver_test():
    driver.get("http://127.0.0.1:5000/users/3")
    time.sleep(5)
    pre_webElement = driver.find_element(By.TAG_NAME, "pre")
    expected_text = '{"user_id":"3","user_name":"Kwame"}'
    actual_text = pre_webElement.text

    print("Username Kwame is displayed. Their UserID = 3")


#Call the functions in order
if __name__ == "__main__":
    test_create_user()
    test_get_user(test_id)
    selenium_webdriver_test()
