import requests

request = requests.get('http://www.paxnet.co.kr/news/main')

html = request.text.strip()

print(html)
