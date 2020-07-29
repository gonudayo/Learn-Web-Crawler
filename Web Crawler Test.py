import requests

request = requests.get('https://www.youtube.com/')

html = request.text.strip()

print(html)
