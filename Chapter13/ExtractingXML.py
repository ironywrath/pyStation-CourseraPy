import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
from urllib.request import urlopen

service_url = 'http://py4e-data.dr-chuck.net/comments_'
full_url = None

while True:
    url_no = input("Please enter the comment number: ")
    if len(url_no) < 1: break

    full_url = service_url + url_no + ".xml"
    print('Retrieving ',full_url)
    xml_data = urlopen(full_url).read()
    print('Retrieved ',len(xml_data),'characters')

    xml_tree = ET.fromstring(xml_data)
    xml_comments = xml_tree.findall('comments/comment')

    comment_count = 0
    comment_num_lst = list()

    for comment in xml_comments:
        comment_count = comment_count + 1
        comment_num_lst.append(int(comment.find('count').text))

    print('Count: ',comment_count)
    print('Sum: ', sum(comment_num_lst))


