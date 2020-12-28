# if __name__ == '__main__':
# import xml.etree.ElementTree as ET
# data = """
# <person>
#     <name>Chuck</name>
#     <phone type="intl">9983751677</phone>
#     <email hide="yes">013himanshu@gmail.com</email>
# </person>
# """
# tree = ET.fromstring(data)
# print("Name:", tree.find("name").text)
# print("Attr:", tree.find("email").get("hide"))

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fetch_url = input("Enter location: ")
print("Retrieving", fetch_url)
url = urllib.request.urlopen(fetch_url).read()
print("Retrieved: " + str(len(url)) + " characters")
tree = ET.fromstring(url)
counts = tree.findall('.//count')
print("Count:", len(counts))
add = 0
for i in counts:
    add = add + int(i.text)
print("Sum:", add)