#!/bin/python3
#import json
#import requests
#from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from os import environ as env

def main():
    print("Starting Chromium... ", end='')
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--disable-features=DefaultPassthroughCommandDecoder")
    chrome_options.add_argument("--no-first-run")
    driver = webdriver.Chrome(options=chrome_options)
    print('OK')

    print("Loading environment variables... ", end='')
    captive_url = env["CAPTIVE_URL"]
    user = env["USER"]
    password = env["PASSWORD"]
    print('OK')

    #Just to ensure that there are no invalid characters in URL
    captive_url = captive_url.replace('"', '')

    print("Fecthing {}... ".format(captive_url), end='')
    driver.get(captive_url)
    print('OK')

    print("Sending User and Pass... ", end='')
    driver.find_element(By.ID, "user").send_keys(user)
    driver.find_element(By.ID, "passwd").send_keys(password)
    driver.find_element(By.ID, "submit").click()
    print('OK')

    print("Done!")

main()
