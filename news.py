import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json


def save_json(file_name, news):
    json_file = json.dumps(news, ensure_ascii=False, sort_keys=True, indent=4).encode('utf8')
    with open(file_name, 'wb') as f:
        f.write(json_file)


def get_news(channel):
    news = []
    for i in channel.findall('item'):
        news.append({'pubDate': i.find('pubDate').text, 'title': i.find('title').text})
    return news


def get_full_news(channel):
    news = []
    for i in channel.findall('item'):
        fields = {}
        for field in i:
            fields[field.tag] = field.text
        news.append(fields)
    return news


data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
channel = root[0]

save_json('news.json', get_news(channel))
save_json('full_news.json', get_full_news(channel))
