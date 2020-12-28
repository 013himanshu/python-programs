import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input("Enter location: ")
    print("Retrieving", url)
    url = urllib.request.urlopen(url).read()
    print("Retrieved", len(url), 'characters')

    try:
        js = json.loads(url)
    except:
        js = None

    if not js:
        print("======= Failure in Retrieving ======")
        print(js)
        continue

    count, add = 0, 0
    for i in js['comments']:
        count = count + 1
        add = add + int(i['count'])

    print('Count:', count)
    print('Sum:', add)
    break

