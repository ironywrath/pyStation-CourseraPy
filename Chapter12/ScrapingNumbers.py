from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
html = urlopen(url, context=ctx).read()

num_lst = list()

soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
for tag in tags:
    num_lst.append(int(tag.contents[0]))

print("Count: ", len(num_lst))
print("Sum: ", sum(num_lst))
