import time

page = 1
page_size = 100

base_url = "https://hub9b8szvc.execute-api.us-east-1.amazonaws.com/prd/products/v1/classifications/WL2-003/products?order_by=41&size={page_size}&agency=01&project_id=01&page={page}&price_min=989000&price_max=4489000"

while True:
    dynamic_url = f"{base_url.format(page_size=page_size, page=page)}"
    print(dynamic_url)
    page += 1
    time.sleep(5)
