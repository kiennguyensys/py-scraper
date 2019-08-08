from selenium import webdriver
import time
from bs4 import BeautifulSoup
import csv

def get_main_info(sorted_products, reviews):
    list = []
    reviews.sort(reverse = True)
    for i in range(len(sorted_products)):
        list.append([sorted_products[i].div.a['href'], reviews[i]])

    return list

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600')

driver = webdriver.Chrome(chrome_options=options)
driver.get("https://dokodemo.world/en/")
more_buttons = driver.find_elements_by_class_name("product_vertical")
page_source = driver.page_source

soup = BeautifulSoup(page_source, 'lxml')
products = soup.find_all('div', class_='product_vertical')
reviews = []
for product in products:
    if product.find_all('div', class_='review')[0].p:
        review = int(product.find_all('div', class_='review')[0].p.span.getText().strip('()'))
        reviews.append(review)
    else:
        reviews.append(0)

sorted_products = [x for (y,x) in sorted(zip(reviews,products), key=lambda pair: pair[0])]
sorted_products.reverse()
for product in sorted_products:
    print(product.find_all('div', class_='review')[0])

main_info = get_main_info(sorted_products, reviews)

with open('dokodemo.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(main_info)
csvFile.close()