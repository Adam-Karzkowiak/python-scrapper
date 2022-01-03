from bs4 import BeautifulSoup
import requests

print("Provide product name")
provided_product_name = input('>')
print(f'Searching for {provided_product_name}')
provided_product_name.replace(" ", "+")
html_text = requests.get(f'https://www.poyerbani.pl/search.php?text={provided_product_name}').text
soup = BeautifulSoup(html_text, 'lxml')
products = soup.find_all('div', class_='product col-6 col-sm-4 col-md-3 pt-3 pb-md-3 mb-3 mb-sm-0')
for product in products:
    product_name = product.find('a', class_='product__name').text
    product_price = product.find('strong', class_='price').text
    product_mapping = product.a['href']
    product_url = f'https://www.poyerbani.pl{product_mapping}'
    print(f"Product name: {product_name}")
    print(f"Product price: {product_price}")
    print(product_url)
