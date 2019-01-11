import base64

a ='526b78425233745561476c7a49476c7a4947566863336b7349484a705a3268305033303d'
print(a.decode('hex'))
print(base64.b64decode(a.decode('hex')))
