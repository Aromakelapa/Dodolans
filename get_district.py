import requests
import json
import os

url = "https://www.jagel.id/api/v3/rajaongkir/get_district.php"
body = {
	"hl": 'in',
	"city" : f"{input('Masukan ID Kota : ')}",
	"token": 'd996af9efa5aefaa2eac4a374e6f03b4'
}

r = requests.post(url, data = body)

try:
	os.mkdir('data')
except:
	pass

son = json.dumps(r.json(), indent=3)
with open('data/district.json', 'w') as file:
	file.write(son)
print('List Kecamatan sudah masuk ke folder data!')