from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import requests
import re

from time import sleep
import json



page = 1

page_size = 100
product_base_infos = []
base_urls = [
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL2-003/products?order_by=41&size={page_size}&agency=01&project_id=01&page={page}&price_min=989000&price_max=4489000", 
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL2-001/products?order_by=41&size={page_size}&agency=01&project_id=01&page={page}&price_min=1989000&price_max=6989000", 
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL2-002/products?order_by=251&size={page_size}&agency=01&project_id=01&page={page}&price_min=1989000&price_max=6689000", 
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL2-004/products?order_by=41&size={page_size}&agency=01&project_id=01&page={page}&price_min=879000&price_max=5789000", 
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL2-006/products?order_by=61&size={page_size}&agency=01&project_id=01&page={page}&price_min=879000&price_max=5689000", 
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL2-005/products?order_by=41&size={page_size}&agency=01&project_id=01&page={page}&price_min=116000&price_max=1989000", 
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL2-007/products?order_by=46&size={page_size}&agency=01&project_id=01&page={page}&price_min=99000&price_max=1599000", 
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL2-070/products?order_by=46&size={page_size}&agency=01&project_id=01&page={page}&price_min=799000&price_max=2399000", 
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL2-034/products?order_by=-1&size={page_size}&agency=01&project_id=01&page={page}&test_ab=8G87oSL3RyqPjkicwnWaqQ&variant_ab=1&price_min=299000&price_max=3899000", 
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL2-009/products?order_by=46&size={page_size}&agency=01&project_id=01&page={page}&price_min=299000&price_max=1299000", 
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL2-053/products?order_by=46&size={page_size}&agency=01&project_id=01&page={page}&price_min=249000&price_max=1599000", 
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL2-008/products?order_by=46&size={page_size}&agency=01&project_id=01&page={page}&price_min=1399000&price_max=1599000", 
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL2-010/products?order_by=269&size={page_size}&agency=01&project_id=01&page={page}&price_min=689000&price_max=9989000", 
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL2-012/products?order_by=36&size={page_size}&agency=01&project_id=01&page={page}&price_min=289000&price_max=1289000", 
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL2-011/products?order_by=36&size={page_size}&agency=01&project_id=01&page={page}&price_min=499000&price_max=2989000", 
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL2-013/products?order_by=36&size={page_size}&agency=01&project_id=01&page={page}&price_min=399000&price_max=3299000", 
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL2-054/products?order_by=36&size={page_size}&agency=01&project_id=01&page={page}&price_min=349000&price_max=699000", 
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL2-016/products?order_by=16&size={page_size}&agency=01&project_id=01&page={page}&price_min=889000&price_max=7589000", 
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL2-015/products?order_by=233&size={page_size}&agency=01&project_id=01&page={page}&price_min=1489000&price_max=13989000", 
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/C200/products?order_by=288&size={page_size}&agency=01&project_id=01&page={page}&test_ab=8G87oSL3RyqPjkicwnWaqQ&variant_ab=1", 
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL2-017/products?order_by=26&size={page_size}&agency=01&project_id=01&page={page}&price_min=128000&price_max=1289000", 
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL2-041/products?order_by=21&ssize={page_size}&agency=01&project_id=01&page={page}&price_min=429000&price_max=1289000", 
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL2-032/products?order_by=16&size={page_size}&agency=01&project_id=01&page={page}&price_min=389000&price_max=1589000", 
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL2-031/products?order_by=6&size={page_size}&agency=01&project_id=01&page={page}&price_min=389000&price_max=1689000", 
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL2-019/products?order_by=41&size={page_size}&agency=01&project_id=01&page={page}&price_min=119000&price_max=649000", 
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL1-005/products?filter_by=%5B%7B%22attribute%22%3A%22Filtro_Medida%22%2C%22value_numeric%22%3Afalse%2C%22values%22%3A%5B%22King+2.00+x+2.00%22%5D%7D%5D&order_by=1&size={page_size}&agency=01&project_id=01&page={page}&price_min=69000&price_max=5794000",
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL1-005/products?filter_by=%5B%7B%22attribute%22%3A%22Filtro_Medida%22%2C%22value_numeric%22%3Afalse%2C%22values%22%3A%5B%22Queen+1.60%22%5D%7D%5D&order_by=1&size={page_size}&agency=01&project_id=01&page={page}&price_min=69000&price_max=5794000",
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL1-005/products?filter_by=%5B%7B%22attribute%22%3A%22Filtro_Medida%22%2C%22value_numeric%22%3Afalse%2C%22values%22%3A%5B%22Doble+1.40%22%5D%7D%5D&order_by=1&size={page_size}&agency=01&project_id=01&page={page}&price_min=69000&price_max=5794000",
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL2-071/products?order_by=1&size={page_size}&agency=01&project_id=01&page={page}&price_min=989000&price_max=2589000", 
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL1-005/products?filter_by=%5B%7B%22attribute%22%3A%22Filtro_Medida%22%2C%22value_numeric%22%3Afalse%2C%22values%22%3A%5B%22Sencillo+0.90%22%2C%22Sencillo+1.00%22%5D%7D%5D&order_by=1&size={page_size}&agency=01&project_id=01&page={page}&price_min=69000&price_max=5794000", 
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL2-037/products?order_by=56&size={page_size}&agency=01&project_id=01&page={page}&price_min=389000&price_max=999000", 
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL2-039/products?order_by=56&size={page_size}&agency=01&project_id=01&page={page}&price_min=389000&price_max=1199000", 
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL2-038/products?order_by=36&size={page_size}&agency=01&project_id=01&page={page}&price_min=289000&price_max=889000", 
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL3-001/products?order_by=66&size={page_size}&agency=01&project_id=01&page={page}&price_min=999000&price_max=3989000", 
    "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL3-012/products?order_by=66&size={page_size}&agency=01&project_id=01&page={page}&price_min=2289000&price_max=2989000"
    ]


# size={page_size}&agency=01&project_id=01&page={page}

for url in base_urls:
    while True:
        product_old_price = ""
        product_current_price = ""
        product_sku = ""
        product_url = ""

        headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9,ru;q=0.8",
        "If-None-Match": "W/\"fb74-ZwenxJRCEOOBjUrP/UAkyij4Ikg\"",
        "Origin": "https://www.jamar.com",
        "Priority": "u=1, i",
        "Referer": "https://www.jamar.com/",
        "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }
        
        product_base_url = f"{url.format(page_size=page_size, page=page)}"
        # print(product_url)

        response = requests.get(product_base_url)

        print(response.status_code)

        data = response.json()
        with open("product.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        products = data["records"]

        for product in products:
            
            try:
                handle_url = product["handle_url"]
            except:
                continue
            try:
                product_old_price = product["price_list"]
                product_current_price = product["capital_price_promo"]
                product_sku = product["sku"]
                print(product_old_price, product_current_price, product_sku)
            except:
                continue
            product_url = "https://www.jamar.com/products/" + f"{handle_url}"
            product_datasheet_url = f'https://jivvtl5cb7.execute-api.us-east-1.amazonaws.com/api/v1/dataSheet/products?sku={product_sku}&projectId=1'
            
            product_base_data = {
                "old_price": product_old_price,
                "current_price":product_current_price,
                "product_url":product_url,
                "datasheet": product_datasheet_url
            }
            
            product_base_infos.append(product_base_data)
                    
        with open("product_base_info.json", "w") as file:
            json.dump(product_base_infos, file, indent=4)
                
        page += 1
        
        if len(products) < page_size:
            page = 1
            break
        
        sleep(10)