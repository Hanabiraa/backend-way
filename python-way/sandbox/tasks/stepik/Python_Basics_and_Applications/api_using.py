"""
task link -> https://stepik.org/lesson/24476/step/3?unit=6781

В этой задаче вам необходимо воспользоваться API сайта numbersapi.com

Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом числе.

Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.
"""

import requests
import json
import sys

template = 'http://numbersapi.com/{}/math?json=true'
for num in sys.stdin:
    resp = requests.get(template.format(num.rstrip()))
    info = json.loads(resp.text)
    answer = 'Interesting' if info['found'] else 'Boring'
    print(answer)

