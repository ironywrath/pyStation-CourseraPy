import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter start name url - ")
repeat_times = input("Please enter repeat process count: ")
name_position = input("Please Enter name position: ")

for counts in range(0,int(repeat_times)):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    tag_loopCount = 0
    for tag in tags:
        #print("Tag Loop: ", tag_loopCount)
        tag_loopCount = tag_loopCount + 1
        if tag_loopCount == int(name_position):
            print("Name:", tag.contents[0], "   ", "URL:", tag.get('href',None))
            url = tag.get('href', None)
            tag_loopCount =1
            break