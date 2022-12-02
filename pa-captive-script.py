#!/bin/python3
import json
import requests
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

FIREFOX_HEADERS = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        }

def old_function:
    with open("config.json", 'r') as file:
        content = json.load(file)
        captive_url = content["captive_url"]
        user = content["user"]
        password = content["password"]
        session = requests.Session()

        response = session.get(
                captive_url,
                verify = False,
                headers = FIREFOX_HEADERS,
                )

        parsed_uri = urlparse(captive_url)
        headers = FIREFOX_HEADERS
        headers["Origin"] = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
        headers["Referer"] = captive_url
        response = session.post(
                captive_url,
                verify=False,
                headers = headers,
                allow_redirects = True,
                data = {
                    "inputStr" : "",
                    "escapeUser" : "",
                    "preauthid" : "",
                    "user" : user,
                    "passwd" : password,
                    "Ok" : "Login",
                    },
                )

        print(json.dumps(dict(response.request.headers), indent=4))
        print(response.status_code)

def new_function():
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    with open("config.json", 'r') as file:
        content = json.load(file)
        captive_url = content["captive_url"]
        user = content["user"]
        password = content["password"]

        driver.find_element_by_id("user").send_keys(user)
        driver.find_element_by_id("passwd").send_keys(user)

        driver.find_element_by_id("submit").click()

new_function()
