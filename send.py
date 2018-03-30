import requests

headers = {}
headers['Authorization'] = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTUyMjUyNTcxMywianRpIjoiNTBhZWY5M2ZlYTQxNGM1YzlhMGY3MDM3MzJlNDIzYWYiLCJ1c2VyX2lkIjoxfQ._b7xXrWqskrrWcDx60-mjsaRmNGUk24XIUO6HAvL3p0'

r = requests.get('http://127.0.0.1:8000/api/token/',headers=headers)

print(r.text)