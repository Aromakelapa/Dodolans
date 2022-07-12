import requests
import json

son = open('data.json')
data = json.load(son)
 
url = 'https://www.jagel.id/api/v3/partner/create_place.php'
print("\nMerchant : " + data['merchant']['name'])
print('\n##### Opening Hours')
print('Jika tutup input 0, jika buka input 1\nJika tutup, jam & menit input -1')
print('Label tersedia : cafe, mie dan bakso, warung, minuman, mie, sarapan, jajanan, promo, penyetan, kue, 24jam, terlaris, jamu, oleh, toko, pakaian, buah, sayur, sembako, satenasgor\n')
body = {
  "token": 'd996af9efa5aefaa2eac4a374e6f03b4',
  "component_view_uid": '6215d6e509e7f',
  "title": data['merchant']['name'],
  "content": data['merchant']['cuisine'],
  "label": f"{input('Label : ')}",
  "origin_address": data['merchant']['address']['combined_address'],
  "origin_lat": data['merchant']['latlng']['latitude'],
  "origin_lng": data['merchant']['latlng']['longitude'],
  "day_1": f"{input('########## Senin : ')}",
  "day1_start_hour": f"{input('# Jam buka : ')}",
  "day1_start_minute": f"{input('Menit : ')}",
  "day1_end_hour": f"{input('# Jam tutup : ')}",
  "day1_end_minute": f"{input('Menit : ')}",
  "day_2": f"{input('########## Selasa : ')}",
  "day2_start_hour": f"{input('# Jam buka : ')}",
  "day2_start_minute": f"{input('Menit : ')}",
  "day2_end_hour": f"{input('# Jam tutup : ')}",
  "day2_end_minute": f"{input('Menit : ')}",
  "day_3": f"{input('########## Rabu : ')}",
  "day3_start_hour": f"{input('# Jam buka : ')}",
  "day3_start_minute": f"{input('Menit : ')}",
  "day3_end_hour": f"{input('# Jam tutup : ')}",
  "day3_end_minute": f"{input('Menit : ')}",
  "day_4": f"{input('########## Kamis : ')}",
  "day4_start_hour": f"{input('# Jam buka : ')}",
  "day4_start_minute": f"{input('Menit : ')}",
  "day4_end_hour": f"{input('# Jam tutup : ')}",
  "day4_end_minute": f"{input('Menit : ')}",
  "day_5": f"{input('########## Jumat : ')}",
  "day5_start_hour": f"{input('# Jam buka : ')}",
  "day5_start_minute": f"{input('Menit : ')}",
  "day5_end_hour": f"{input('# Jam tutup : ')}",
  "day5_end_minute": f"{input('Menit : ')}",
  "day_6": f"{input('########## Sabtu : ')}",
  "day6_start_hour": f"{input('# Jam buka : ')}",
  "day6_start_minute": f"{input('Menit : ')}",
  "day6_end_hour": f"{input('# Jam tutup : ')}",
  "day6_end_minute": f"{input('Menit : ')}",
  "day_7": f"{input('########## Minggu : ')}",
  "day7_start_hour": f"{input('# Jam buka : ')}",
  "day7_start_minute": f"{input('Menit : ')}",
  "day7_end_hour": f"{input('# Jam tutup : ')}",
  "day7_end_minute": f"{input('Menit : ')}",
  "hl": 'in',
  "working_hour": '0',
  "hide_image_flag": '0',
  "by_appointment": '0',
  "set_origin_flag": '1',
  "style": '0',
  "purchasable": '0',
  "price": '0',
  "appuid": '5f3e3c3c77909'
}

y = "y"

if input('Lanjut input y : ') == y:
  r = requests.post(url, data=body)

  print(r.status_code)
  print()
  # print(r.json())
  # print(json.dumps(body, indent=2))
else:
  pass



# Hiraukan
# Data Images
# print()

# with open('response.json', 'w') as file:
#   file.write(json.dumps(r.json(), indent=3))
#   file.close

# rJson = json.load(open('response.json', 'r'))
# rTitle = rJson['list']['title'].replace(' ', '+')

# image = open('image.txt', 'r').read()

# with open('data.txt', 'w') as file:
#   file.write(image)
#   file.close

# asu = f"&hl=in&view_uid={rJson['list']['view_uid']}&appuid=5f3e3c3c77909&position=0&title={rTitle}&token=d996af9efa5aefaa2eac4a374e6f03b4&image_type=jpg&"
# with open('data.txt', 'a') as file:
#   file.write(asu)
#   file.close

# # data = open('data.txt', 'r').read()