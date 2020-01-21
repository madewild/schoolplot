"""Extracting school addresses from enseignement.be"""

import sys
import re
import requests
from bs4 import BeautifulSoup

degree = sys.argv[1]
if degree == "prim":
    num = 2
elif degree == "sec":
    num = 3
else:
    print("Unknown degree")
    sys.exit()

output = open(f"data/{degree}_addresses.tsv", "w")
header = "name\taddress\n"
output.write(header)

url = f"http://www.enseignement.be/index.php?page=2593{num}&act=search&check=&unite=&geo_type=1&geo_prov=5&geo_cp=&geo_loca=&geo_mots=&reseau=111%2C126%2C123%2C122%2C121%2C131%2C132&opt_degre=&opt_tyen=&opt_domaine=0&opt_mots=&opt_groupe=11&opt_option="
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
    output_string = f"{name}\t{address}\n"
    if cp.startswith("6") or cp.startswith("7"):
        output.write(output_string)
output.close()
