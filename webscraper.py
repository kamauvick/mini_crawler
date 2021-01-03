from typing import Container
import requests
from bs4 import BeautifulSoup as soup
import csv

my_url = "https://www.jumia.co.ke/smart-tvs-2282/"
filename = "Jumia_Tv_data.csv"
return_data = []


def webScraper():
    response  = requests.get(my_url)
    page_data = response.text
    parsed_data = soup(page_data, "html.parser")
    product_data = parsed_data.findAll("div", {"class": "info"})

    for container_data in product_data:
        try:
            raw_product_names = container_data.findAll("h3", {"class": "name"})
            product_name = raw_product_names[0].text
            raw_new_product_price = container_data.findAll("div", {"class": "prc"})
            new_product_price = raw_new_product_price[0].text

            with open(filename, 'w') as _data_file:
                data_writer = csv.writer(_data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                data_writer.writerow(["Product Name", "New Product Price", "Old product Price", "Product Discount"])
                data_writer.writerow([product_name, new_product_price,])

            product_data = {
                "Object details": "Jumia TV sets product data",
                "Author": "Vick",
                "product_name": product_name,
                "new_product_price": new_product_price,
            }
            
            return_data.append(product_data)
        except:
            print("Opps 1")
        # try:
        #     raw_old_product_price = container_data.findAll("div", {"class": "old"})
        #     old_product_price = raw_old_product_price[0].text
        # except:
        #     print("WARNING 1")
        # try:
        #     raw_product_discount = container_data.findAll("div", {"class": "tag _dsct _sm"})
        #     product_discount = raw_product_discount[0].text
        # except:
        #     print("Error 3")
   

        
        
        # print(f'Old Product Price: {old_product_price}')
        # print(f'Product Discount: {product_discount} \n')
    return return_data

my_data = webScraper()
print(type(my_data))