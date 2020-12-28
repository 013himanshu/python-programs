# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(("data.pr4e.org", 80))
# cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
# mysock.send(cmd)
#
# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode())
# mysock.close()


# import urllib.error, urllib.parse, urllib.request
# fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
# for line in fhand:
#     print(line.decode().strip())

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# url = input("Enter URL: ")
# html = urllib.request.urlopen(url)
# soup = BeautifulSoup(html, "html.parser")
# tags = soup("a")
# for tag in tags:
#     print(tag.get("href", None))

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import ssl
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = "http://py4e-data.dr-chuck.net/comments_1001417.html"
# html = urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, "html.parser")
#
# # Retrieve all of the anchor tags
# tags = soup('span')
# result = 0
# for tag in tags:
#     result = result + int(tag.contents[0])
#
# print(result)

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')
count = int(input('Enter count:'))
position = int(input('Enter position:'))-1
html = urlopen(url).read()

soup = BeautifulSoup(html,"html.parser")
href = soup('a')
#print href

for i in range(count):
    link = href[position].get('href', None)
    print(href[position].contents[0])
    html = urlopen(link).read()
    soup = BeautifulSoup(html,"html.parser")
    href = soup('a')

