import requests
import json

url = f'https://p.grabtaxi.com/api/passenger/v4/grabfood/merchants/{input("ID Merchant : ")}?latlng=-6.890702%2C109.676352'

head = {
	"x-request-id": "7213abd6-3ed8-43d9-90e9-095bbb47d893",
	"Accept-Language": "in-ID;q=1.0, en-US;q=0.9, en;q=0.8",
	"User-Agent": "Grab/5.204.0 (Android 11; Build 34436267)",
	"x-mts-ssid": "eyJhbGciOiJSUzI1NiIsImtpZCI6Il9kZWZhdWx0IiwidHlwIjoiSldUIn0.eyJhdWQiOiJQQVNTRU5HRVIiLCJlc2kiOiJrT1AvTGtPNitYLzltVTJYbGtmTHllVVdLSC9QdzhKL2tyRXNqYlArR2RabjMwL0tyUT09IiwiZXhwIjo0ODA4NzEwMjc2LCJpYXQiOjE2NTUxMTAyNzMsImp0aSI6Ijg2NTBhMTgxLTMwNjEtNDk0NC1iM2QzLTAxNWNlZDExYTA3NSIsImxtZSI6IkdPT0dMRVYzIiwibmFtZSI6IiIsInN1YiI6ImIxNTRiODVkLTYzMDAtNGJmMS05MTBmLWJjNjAyN2M1ZGRjYiJ9.uJeQmWXcUaXFK8S51zvoQjA4bfpl02KHJ6UYIMqo_fXRXFzi6gDc-Gqe4m2pdmN5iS1wmFXtGiUSEztQol-e1NtLlTLDTroYHzVAbCLZcsnwhlTvk2gz48Esy8MwF5pZ89u2JHN3aFl8pyXmLYyI-tg-JHpEiUoLQ82Kuu8lXXZioMUJgbGalr2-WZqnrUgQo0tRfkGVWn32z03W4LYQ856pIpy5TBUIiOWyfVQ991Fxb3WjmXhBhQhJXOcHBxXQqAInqZeLx5WCEQsUEYMgCPTigwY3pbFuhA9x37Ge1YvLGf88_zTQILc2u7P_L-0yMeqEGbPHHu-i8fi7DRqdudhQxUlw_KvQtOS_D0AtLqGlz5Gwx2y_ZxLIbSUhwok26lPlMDRfqQvPFKF7KnqH9PBL3PGxJDMmhTKbaxo538nQa_yf9uhx3ydmVHsk_oTvx79qyeuNKYsVVsBv5lyywnnIfASTONC1EKOVGEroCCScnwtwHos2hz51b_nk47N8d_3DT9p5FSyxkOuzZSBe7fdsBHHysQUaoUOa5U736dyuTdHCjtk-lKp80MzcHoeVNQofJolg7kXKVxdToBH2leuVNE_Irz9FnL0OIFzHqtpFDH5WDF78EraYoo9JlUPmkdfHQ4zWFP6ujhRawmZGwPGk5tlk8BePNzuJ3iRutg8",
	"Host": "p.grabtaxi.com",
	"Connection": "close",
	"Accept-Encoding": "gzip, deflate"
}

r = requests.get(url, headers=head)

print(r.status_code)
print()
# print(r.json())
data = json.dumps(r.json(), indent=3)
with open('data.json', mode='w') as file:
	file.write(data)
	file.close
# print(data['merchant']['name'])