import requests, json

creds_path = r'PATH-TO-API-TOKEN'

with open(creds_path) as f:
    creds = json.load(f)

store_url = "YOUR-SHOPIFY-ADMIN-STORE-URL"

endpoint = "/admin/oauth/access_scopes.json"

full_url = "https://{}.myshopify.com{}".format(store_url,endpoint)

headers_values = {'Content-type':'application/json','X-Shopify-Access-Token':creds['token']}

r = requests.get(full_url,headers=headers_values)

response = json.loads(r.content)

print(response)
