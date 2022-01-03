from bs4 import BeautifulSoup
import requests
import time

print("Provide product name")
provided_product_name = input('>')
print(f'Searching for {provided_product_name}')


def find_products():
    provided_product_name.replace(" ", "+")
    html_text = requests.get(f'https://www.poyerbani.pl/search.php?text={provided_product_name}').text
    soup = BeautifulSoup(html_text, 'lxml')
    products = soup.find_all('div', class_='product col-6 col-sm-4 col-md-3 pt-3 pb-md-3 mb-3 mb-sm-0')
    for index, product in enumerate(products):
        product_name = product.find('a', class_='product__name').text
        product_price = product.find('strong', class_='price').text
        product_mapping = product.a['href']
        product_url = f'https://www.poyerbani.pl{product_mapping}'
        with open(f'posts/{index}.txt', 'w') as f:
            f.write(f"Product name: {product_name} \n")
            f.write(f"Product price: {product_price} \n")
            f.write(f"Product url: {product_url}")
        print(f'Filve saved: {index}')


if __name__ == '__main__':
    while True:
        find_products()
        time_wait = 10
        print(f'Waiting {time_wait} minutes....')
        time.sleep(time_wait * 60)
