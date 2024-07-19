import requests, json
from bs4 import BeautifulSoup

product_base_info =[ 
    {
        "old_price": 5144250,
        "current_price": 2989000,
        "product_url": "https://www.jamar.com/products/cuna-para-bebe-1-00-anny-natural-off-white-7030385",
        "datasheet": "https://jivvtl5cb7.execute-api.us-east-1.amazonaws.com/api/v1/dataSheet/products?sku=7030385&projectId=1"
    }
]

url = product_base_info[0]["product_url"]
data_url = product_base_info[0]["datasheet"]

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

results = []
product_price = product_base_info[0]["current_price"]

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
                    print(product_alto)
                elif item["title"] == "Ancho":
                    product_ancho = item["value"]
                    print(product_ancho)
                elif item["title"] == "Profundo":
                    product_profundo = item["value"]
                    print(product_profundo)
                elif item["title"] == "Número Puestos":
                    product_numero_puestos = item["value"]
                    print(product_numero_puestos)
                elif item["title"] == "Medidas Sofá 1 (Alto X Ancho X Profundidad)":
                    product_mediadas_sofa1 = item["value"]
                    print(product_mediadas_sofa1)
                elif item["title"] == "Medidas Butaco (A) (Alto X Ancho X Profundidad)":
                    product_medidas_butaco = item["value"]
                    print(product_medidas_butaco)
                elif item["title"] == "Medidas Puff (Alto X Ancho X Profundidad)":
                    product_medidas_puff = item["value"]
                    print(product_medidas_puff)
                elif item["title"] == "Medidas Producto Extendido (Alto X Ancho X Profundidad)":
                    product_producto_extendido = item["value"]
                    print(product_producto_extendido)
                elif item["title"] == "Medidas Mesa Comedor (Alto X Ancho X Profundidad)":
                    product_masa_comedor = item["value"]
                    print(product_masa_comedor)
                elif item["title"] == "Medidas Silla (Alto X Ancho X Profundidad)":
                    product_medidas_silla = item["value"]
                    print(product_medidas_silla)
                elif item["title"] == "Medidas Cama (Alto X Ancho X Profundidad)":
                    product_medidas_cama = item["value"]
                    print(product_medidas_cama)
                elif item["title"] == "Tamaño":
                    product_tamano = item["value"]
                    print(product_tamano)
                elif item["title"] == "Medidas Nochero (Alto X Ancho X Profundidad)":
                    product_medidas_nochero = item["value"]
                    print(product_medidas_nochero)
                elif item["title"] == "Medidas Tocador / Espejo (Alto X Ancho X Profundidad)":
                    product_medidas_tocador = item["value"]
                    print(product_medidas_tocador)
                elif item["title"] == "":
                    product_ = item["value"]
                    print(product_)
                # Colors 
                elif item["title"] == "Color Estructura":
                    product_estructura_color = item["value"]
                    print(product_estructura_color)
                elif item["title"] == "Color Tapiz":
                    product_tapiz_color = item["value"]
                    print(product_tapiz_color)
                elif item["title"] == "":
                    product_ = item["value"]
                    print(product_)
                
                # Materials
                elif item["title"] == "Material De La Estructura":
                    product_material_estructura = item["value"]
                    print(product_material_estructura)
                elif item["title"] == "Material Del Relleno":
                    product_material_relleno = item["value"]
                    print(product_material_relleno)
                elif item["title"] == "Acabado":
                    product_acabado = item["value"]
                    print(product_acabado)
                elif item["title"] == "Composición":
                    product_composicion = item["value"]
                    print(product_composicion)
                elif item["title"] == "Tipo De Pata":
                    product_tipo_pata = item["value"]
                    print(product_tipo_pata)
                elif item["title"] == "Tipo Tela Sap":
                    product_tipo_tela_sap = item["value"]
                    print(product_tipo_tela_sap)
                elif item["title"] == "Patas Desmontables":
                    product_patas_desmontables = item["value"]
                    print(product_patas_desmontables)
                elif item["title"] == "Manijas":
                    product_manijas = item["value"]
                    print(product_manijas)
                elif item["title"] == "Cantidad De Cajones":
                    product_cantidad_cajones = item["value"]
                    print(product_cantidad_cajones)
                elif item["title"] == "Número De Puertas":
                    product_material_numero_puestos = item["value"]
                    print(product_material_numero_puestos)
                elif item["title"] == "Cantidad De Repisas":
                    product_cantidad_repisas = item["value"]
                    print(product_cantidad_repisas)
                elif item["title"] == "Riel Telescópico":
                    product_riel_telescopico = item["value"]
                    print(product_riel_telescopico)
                elif item["title"] == "Espejo":
                    product_espejo = item["value"]
                    print(product_espejo)
                elif item["title"] == "Ruedas":
                    product_ruedas = item["value"]
                    print(product_ruedas)
                elif item["title"] == "Tubos Colgaderos":
                    product_tubos_colgaderos = item["value"]
                    print(product_tubos_colgaderos)
                elif item["title"] == "Tipo De Espuma":
                    product_tipo_espuma = item["value"]
                    print(product_tipo_espuma)
                elif item["title"] == "Tipo Colchon Sap":
                    product_tipo_colchon = item["value"]
                    print(product_tipo_colchon)
                elif item["title"] == "Filtro Firmeza":
                    product_nivel_firmeza = item["value"]
                    print(product_nivel_firmeza)
                elif item["title"] == "Nivel Ortopedico":
                    product_nivel_ortopedico = item["value"]
                    print(product_nivel_ortopedico)
                elif item["title"] == "Movilidad Baranda/Barandas Removibles":
                    product_movilidad_baranda = item["value"]
                    print(product_movilidad_baranda)
                elif item["title"] == "Protector De Encías":
                    product_protector_encias = item["value"]
                    print(product_protector_encias)
                elif item["title"] == "":
                    product_ = item["value"]
                    print(product_)
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