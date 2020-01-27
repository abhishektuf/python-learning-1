import requests
from bs4 import BeautifulSoup
from subprocess import run

URL = 'https://www.amazon.in/dp/B07X2KLYS2/ref=cm_sw_r_tw_dp_U_x_mqtkEbWG8DJ05'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36 Edg/79.0.309.71'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')


title = soup.find(id="productTitle").get_text()

price = soup.find(id="priceblock_ourprice").get_text()

converted_price=price[0:12]

print(converted_price)

title = title.strip()

title = title.capitalize()

print(title)