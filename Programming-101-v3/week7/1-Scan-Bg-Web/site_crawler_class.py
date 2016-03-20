import requests
from histogram_class import Histogram
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np


website = "http://register.start.bg/"
my_request = requests.get(website)

# print (my_request.headers["Server"])

soup = BeautifulSoup(my_request.text)

# bg_sites = soup.find_all(soup.span['onclick '])
# bg_sites = soup.span['onclick's]

# bg_sites = soup.find_all('a', 'href')
# bg_sites = []
id_sites = []

histogram_sites = Histogram()

counter = 0
for link in soup.find_all('a'):
    # bg_sites.append(link.get('href'))

    if 'link.php' in str(link.get('href')):
        if len(id_sites) < 50:
            id_sites.append(str(link.get('href')))

for i in id_sites:
    current_website = website + str(i)
    try:
        current_request = requests.head(
            current_website, allow_redirects=True, timeout=2)
        if current_request.ok is True:
            current_server = current_request.headers["Server"]
            if 'Apache' in str(current_server):
                histogram_sites.add('Apache')
                continue
            if 'nginx' in str(current_server):
                histogram_sites.add('nginx')
                continue
            histogram_sites.add(current_request.headers["Server"])
    except:
        pass


result = histogram_sites.get_dict()

for key, count in result.items():
    print("{}: {}".format(key, count))


keys = list(result.keys())
values = list(result.values())

X = list(range(len(keys)))

plt.bar(X, list(result.values()), align="center")
plt.xticks(X, keys)

plt.title(".bg servers")
plt.xlabel("Server")
plt.ylabel("Count")


plt.show()
