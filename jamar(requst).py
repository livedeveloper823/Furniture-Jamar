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

results = []
for product_base_info in product_base_infos:

    url = product_base_info["product_url"]
    data_url = product_base_info["datasheet"]

    # Daclare Variables
    product_name =""
    product_price = ""
    img_url = ""
    # Medidas
    product_alto = ""
    product_ancho = ""
    product_profundo = ""
    product_numero_puestos = ""
    product_mediadas_sofa1 = ""
    product_medidas_butaco = ""
    product_medidas_puff = ""
    product_producto_extendido = ""
    product_masa_comedor = ""
    product_medidas_silla = ""
    product_medidas_cama = ""
    product_tamano = ""
    product_medidas_nochero = ""
    product_medidas_tocador = ""
    # Colors 
    product_estructura_color = ""
    product_tapiz_color = ""
    # Materials
    product_material_estructura = ""
    product_material_relleno = ""
    product_acabado = ""
    product_composicion = ""
    product_tipo_pata = ""
    product_tipo_tela_sap = ""
    product_patas_desmontables = ""
    product_manijas = ""
    product_cantidad_cajones = ""
    product_material_numero_puestos = ""
    product_cantidad_repisas = ""
    product_riel_telescopico = ""
    product_espejo = ""
    product_ruedas = ""
    product_tubos_colgaderos = ""
    product_tipo_espuma = ""
    product_tipo_colchon = ""
    product_nivel_firmeza = ""
    product_nivel_ortopedico = ""
    product_movilidad_baranda = ""
    product_protector_encias = ""

    product_price = product_base_info["current_price"]

    res = requests.get(url)

    print(res.status_code)
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, "html.parser")
        product = str(soup).split("productObj =")[1].split(";\n")[0]
        with open("product.html", "w", encoding="utf-8") as file:
            file.write(str(soup))
            
        product_data = json.loads(product)
        product_num = product_data["variants"][0]["sku"]
        product_name = str(product_data["title"]).split(",")[0]
        img_url = str(product_data["images"][0]).split("?")[0]
        description = product_data["content"]
        print(product_num, img_url)
        print(product_name)
        print(description)

    else:
        pass

    response = requests.get(data_url)
    print("Datasheet =====>",response.status_code)

    if response.status_code == 200:
        data_soup = BeautifulSoup(response.content, "html.parser")
        with open("product1.json", "w", encoding="utf-8") as file:
            file.write(str(data_soup))
        product_data = json.loads(str(data_soup))
        for product in product_data:
            for item in product["items"]:
                try:
                    # Medidas
                    if item["title"] == "Alto":
                        product_alto = item["value"]
                    elif item["title"] == "Ancho":
                        product_ancho = item["value"]
                    elif item["title"] == "Profundo":
                        product_profundo = item["value"]
                    elif item["title"] == "Número Puestos":
                        product_numero_puestos = item["value"]
                    elif item["title"] == "Medidas Sofá 1 (Alto X Ancho X Profundidad)":
                        product_mediadas_sofa1 = item["value"]
                    elif item["title"] == "Medidas Butaco (A) (Alto X Ancho X Profundidad)":
                        product_medidas_butaco = item["value"]
                    elif item["title"] == "Medidas Puff (Alto X Ancho X Profundidad)":
                        product_medidas_puff = item["value"]
                    elif item["title"] == "Medidas Producto Extendido (Alto X Ancho X Profundidad)":
                        product_producto_extendido = item["value"]
                    elif item["title"] == "Medidas Mesa Comedor (Alto X Ancho X Profundidad)":
                        product_masa_comedor = item["value"]
                    elif item["title"] == "Medidas Silla (Alto X Ancho X Profundidad)":
                        product_medidas_silla = item["value"]
                    elif item["title"] == "Medidas Cama (Alto X Ancho X Profundidad)":
                        product_medidas_cama = item["value"]
                    elif item["title"] == "Tamaño":
                        product_tamano = item["value"]
                    elif item["title"] == "Medidas Nochero (Alto X Ancho X Profundidad)":
                        product_medidas_nochero = item["value"]
                    elif item["title"] == "Medidas Tocador / Espejo (Alto X Ancho X Profundidad)":
                        product_medidas_tocador = item["value"]
                    elif item["title"] == "":
                        product_ = item["value"]
                    # Colors 
                    elif item["title"] == "Color Estructura":
                        product_estructura_color = item["value"]
                    elif item["title"] == "Color Tapiz":
                        product_tapiz_color = item["value"]
                    elif item["title"] == "":
                        product_ = item["value"]
                    
                    # Materials
                    elif item["title"] == "Material De La Estructura":
                        product_material_estructura = item["value"]
                    elif item["title"] == "Material Del Relleno":
                        product_material_relleno = item["value"]
                    elif item["title"] == "Acabado":
                        product_acabado = item["value"]
                    elif item["title"] == "Composición":
                        product_composicion = item["value"]
                    elif item["title"] == "Tipo De Pata":
                        product_tipo_pata = item["value"]
                    elif item["title"] == "Tipo Tela Sap":
                        product_tipo_tela_sap = item["value"]
                    elif item["title"] == "Patas Desmontables":
                        product_patas_desmontables = item["value"]
                    elif item["title"] == "Manijas":
                        product_manijas = item["value"]
                    elif item["title"] == "Cantidad De Cajones":
                        product_cantidad_cajones = item["value"]
                    elif item["title"] == "Número De Puertas":
                        product_material_numero_puestos = item["value"]
                    elif item["title"] == "Cantidad De Repisas":
                        product_cantidad_repisas = item["value"]
                    elif item["title"] == "Riel Telescópico":
                        product_riel_telescopico = item["value"]
                    elif item["title"] == "Espejo":
                        product_espejo = item["value"]
                    elif item["title"] == "Ruedas":
                        product_ruedas = item["value"]
                    elif item["title"] == "Tubos Colgaderos":
                        product_tubos_colgaderos = item["value"]
                    elif item["title"] == "Tipo De Espuma":
                        product_tipo_espuma = item["value"]
                    elif item["title"] == "Tipo Colchon Sap":
                        product_tipo_colchon = item["value"]
                    elif item["title"] == "Filtro Firmeza":
                        product_nivel_firmeza = item["value"]
                    elif item["title"] == "Nivel Ortopedico":
                        product_nivel_ortopedico = item["value"]
                    elif item["title"] == "Movilidad Baranda/Barandas Removibles":
                        product_movilidad_baranda = item["value"]
                    elif item["title"] == "Protector De Encías":
                        product_protector_encias = item["value"]
                    elif item["title"] == "":
                        product_ = item["value"]
                except:
                    pass
                
    product_json = {
        "Nombre":product_name,
        "Precio":product_price,
        "Img_url":img_url,
        # Medidas
        "Alto":product_alto,
        "Ancho":product_ancho,
        "Profundo":product_profundo,
        "Número de puertas":product_numero_puestos,
        "Medidas Sofa 1":product_mediadas_sofa1,
        "Butaco":product_medidas_butaco,
        "Puff":product_medidas_puff,
        "Producto Extendido":product_producto_extendido,
        "Masa Comedor":product_masa_comedor,
        "Silla":product_medidas_silla,
        "Cama":product_medidas_cama,
        "Tamano":product_tamano,
        "Nochero":product_medidas_nochero,
        "Tocador":product_medidas_tocador,
        # Colors 
        "Color del esstructura":product_estructura_color,
        "Color del tapiz":product_tapiz_color,
        # Materials
        "Material Estructura":product_material_estructura,
        "Material Relleno":product_material_relleno,
        "Acabado":product_acabado,
        "Composicion":product_composicion,
        "Tipo de Pata":product_tipo_pata,
        "Tipo Tela Sap":product_tipo_tela_sap,
        "Patas Desmontables":product_patas_desmontables,
        "Manijas":product_manijas,
        "Cantidad de Cajones":product_cantidad_cajones,
        "Numero de Piestos":product_material_numero_puestos,
        "Cantidad Repisas":product_cantidad_repisas,
        "Riel Telesopico":product_riel_telescopico,
        "Espejo":product_espejo,
        "Ruedas":product_ruedas,
        "Tubos Colgaderos":product_tubos_colgaderos,
        "Tipo Espuma":product_tipo_espuma,
        "Tipo Colchon":product_tipo_colchon,
        "Nivel de firmeza":product_nivel_firmeza,
        "Nivel ortopedico":product_nivel_ortopedico,
        "Movilidad Baranda":product_movilidad_baranda,
        "Protector Encias":product_protector_encias,
    } 
    results.append(product_json)

    import os, csv
    if not os.path.exists("./results"):
        os.makedirs("./results")

    with open("./results/jamar.json", "w") as file:
        json.dump(results, file, indent=4)

    # JSON data
    with open("./results/jamar.json", "r") as file:
        json_data = json.load(file)

    # Define CSV file name
    csv_file = "./results/jamar.csv"

    # Define fieldnames for CSV header
    fieldnames = json_data[0].keys()

    # Write JSON data to CSV
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in json_data:
            writer.writerow(item)