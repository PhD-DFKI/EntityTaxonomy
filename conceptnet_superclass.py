import requests

obj = requests.get('http://api.conceptnet.io/c/en/Swan').json()
#obj = requests.get('http://api.conceptnet.io/c/en/animal').json()
#obj = requests.get('http://api.conceptnet.io/c/en/Train').json()
#obj = requests.get('http://api.conceptnet.io/c/en/Berlin').json()
print(obj)
print("IsA Relations:")
print([edge['end']['@id'] for edge in obj['edges']])


