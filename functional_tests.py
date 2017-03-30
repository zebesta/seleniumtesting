from selenium import webdriver
import os

# import the chrome driver from the local directory 
chromedriver = "./chromedriver"
browser = webdriver.Chrome(chromedriver)
browser.get('http://localhost:8000')
assert 'Django' in browser.title
