import requests, json
from pprint import pprint

creds_path = r'PATH-TO-API-TOKEN'

with open(creds_path) as f:
    creds = json.load(f)

store_url = "YOUR-SHOPIFY-STORE-URL"

# 2024-01-01T00:00:00-05:00

endpoint = "/admin/api/2024-07/orders.json?status=any&created_at_min=2024-01-01T00:00:00-05:00&fields=total_price,name,id,email,created_at"

full_url = "https://{}.myshopify.com{}".format(store_url,endpoint)

headers_values = {'Content-type':'application/json','X-Shopify-Access-Token':creds['token']}

r = requests.get(full_url,headers=headers_values)

response = json.loads(r.content)

pprint(response)
