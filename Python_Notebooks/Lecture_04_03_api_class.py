import requests

BASE = "https://dummyjson.com"

def pretty(title, r):
    print("\n==============================")
    print(title)
    print("==============================")
    print("Status:", r.status_code)
    print("URL:", r.url)
    print("Response JSON:")
    print(r.json())


# 1) Show product list (GET all)
resp_all = requests.get(f"{BASE}/products")
pretty("GET ALL PRODUCTS", resp_all)


# 2) Pick one product (GET by id)
product_id = 1
resp_id = requests.get(f"{BASE}/products/{product_id}")
pretty(f"GET PRODUCT BY ID = {product_id}", resp_id)


# 3) Search products (GET with query)
query = "phone"
resp_search = requests.get(f"{BASE}/products/search", params={"q": query})
pretty(f"SEARCH PRODUCTS BY QUERY = '{query}'", resp_search)


# 4) Create a new product (POST)
new_product = {
    "title": "Demo Product",
    "price": 1000,
    "description": "Created during API demo",
    "category": "teaching"
}

resp_post = requests.post(f"{BASE}/products/add", json=new_product)
pretty("CREATE NEW PRODUCT (POST)", resp_post)
