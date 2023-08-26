
from flask import Flask, request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from config import config

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home'

@app.route('/search')
def search():
    query = request.args['query']
    se = request.args['se']

    service = Service()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--verbose')
    options.add_argument('--no-sandbox')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(service=service, options=options)

    results = {}
    
    if se == 'google':
        print('[*] Work in progress...')
        return {}
    elif se == 'ddg':
        url = config.search_engine['duckduckgo']['domain'] + query
        driver.get(url)
        matches = driver.find_elements(By.TAG_NAME, 'article')
    else:
        print('[*] Oof... Unknown se supplied.')
        return results
        
    for i in range(len(matches)):
        config.search_results.append(matches[i].text.split('\n'))
        
    for i in range(len(config.search_results)):
        results[i] = {
            'url': config.search_results[i][0],
            'heading': config.search_results[i][1],
            'subheading': config.search_results[i][2]
        }
    
    return results
