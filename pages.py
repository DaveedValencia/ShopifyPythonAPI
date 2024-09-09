import requests, json

creds_path = r"PATH-TO-API-TOKEN"

with open(creds_path) as f:
    creds = json.load(f)

header_values = {'Content-Type': 'application/json','X-Shopify-Access-Token':creds['token']}

store_url = "SHOPIFY-URL"

orders_endpoint = "/admin/api/2024-07/orders.json?"

first_params = "status=any&limit=1&fields=id,name,created_at"

def build_url(store,endpoint,params):
    full_url = "https://{}.myshopify.com{}{}".format(store,endpoint,params)
    return full_url

first_url = build_url(store_url,orders_endpoint,first_params)

first_call = requests.get(first_url,headers=header_values)

first_content = json.loads(first_call.content)
print(first_content)
print()

first_headers = first_call.headers["Link"]

def get_next(links):
    link_list = links.split(',')
    for link in link_list:
        if 'rel="next"' in link:
            page_info = link.split('page_info=')
            page_info = page_info[1].split('>')[0]
            return page_info
        
next_link = get_next(first_headers)

second_params = "limit=1&fields=id,name,created_at&page_info={}".format(next_link)

second_url = build_url(store_url,orders_endpoint,second_params)

second_call = requests.get(second_url,headers=header_values)

second_content = json.loads(second_call.content)
second_headers = second_call.headers["Link"]

print(second_content)
