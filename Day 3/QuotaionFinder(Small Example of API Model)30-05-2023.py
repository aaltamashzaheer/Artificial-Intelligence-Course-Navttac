import requests
response = requests.get('https://zenquotes.io/api/random')
if response.status_code == 200:
    data=response.json()
    print(data)
    quote=data[0]['q']
    author=data[0]['a']
    print(f'{quote} - {author}')
else:
    print('Error Occured',response.status_code)