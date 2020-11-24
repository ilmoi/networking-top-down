import urllib.request
import requests

DOMAIN = '127.0.0.1'  # todo
PORT = 9000  # todo

# option 1
fhand = urllib.request.urlopen(f"http://{DOMAIN}:{PORT}")
for line in fhand:
    print(line.decode().strip())

# option 2
data = requests.get(f"http://{DOMAIN}:{PORT}")
print(data.text)
