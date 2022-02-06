"""
task link -> https://stepik.org/lesson/24471/step/7?unit=6780
"""

import re
import requests

# url = input()
url = 'https://yandex.ru/search/?text=dasda&lr=2'
resp = requests.get(url)

links = set()
pattern = re.compile(r'<a.*?href=".*?:\/\/((?:\w|-)+(?:\.(?:\w|-)+)+)')
for link in pattern.findall(resp.text):
    links.add(link)
print(*sorted(links), sep='\n')