"""Extracting school addresses from enseignement.be"""

import sys
import re
import requests
from bs4 import BeautifulSoup

url_file = open("urls.csv").readlines()
urls = {}
for line in url_file:
    domain, url = line.strip().split(",")
    urls[domain] = url

degree = sys.argv[1]
if degree == "fond":
    url = urls["fondamental ordinaire"]
elif degree == "sec":
    url = urls["secondaire ordinaire"]
else:
    print("Specialised is not handled yet")
    sys.exit()

output = open(f"data/{degree}_addresses.tsv", "w")
header = "name\taddress\n"
output.write(header)

html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
html_table = soup.find("table", attrs={"class": "tbl_lll tbl_listing"})
schools = html_table.tbody.find_all("tr")
for school in schools:
    fields = [td.text for td in school.find_all("td")]
    name = fields[0].strip()
    name = name.replace('"', '')
    street = fields[1].strip()
    street = re.sub(r'\s+', " ", street)
    street = street.replace(" , ", " ")
    street = street.replace("Bld", "Boulevard")
    street = street.replace("Av ", "Avenue ")
    cp = fields[2].strip()
    city = fields[3].strip()
    address = f"{street}, {cp} {city}, Belgium"
    if "SHAPE" in address:
        address = "SHAPE, Mons, Belgium"
    output_string = f"{name}\t{address}\n"
    if int(cp) in range(7000,7400):
        output.write(output_string)
output.close()
