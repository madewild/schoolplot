"""Extracting school addresses from enseignement.be"""

import requests

secondary_url = "http://www.enseignement.be/index.php?page=25933&act=search&check=&unite=&geo_type=1&geo_prov=5&geo_cp=&geo_loca=&geo_mots=&reseau=111%2C126%2C123%2C122%2C121%2C131%2C132&opt_degre=&opt_tyen=&opt_domaine=0&opt_mots=&opt_groupe=11&opt_option="
r = requests.get(secondary_url)
html = r.content
output = open("schools.tsv", "r")