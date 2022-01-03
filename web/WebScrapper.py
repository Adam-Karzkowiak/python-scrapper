from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.poyerbani.pl/search.php?text=yerba+mate').text
soup = BeautifulSoup(html_text, 'lxml')
product = soup.find('div', class_='product col-6 col-sm-4 col-md-3 pt-3 pb-md-3 mb-3 mb-sm-0')
product_name = product.find('a', class_='product__name').text
product_price = product.find('strong', class_='price').text
print(f'Name: {product_name} || Price: {product_price}')