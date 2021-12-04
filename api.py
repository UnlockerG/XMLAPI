from urllib.request import urlopen
from urllib.parse import quote
from json import loads
from itertools import groupby


def get_date(page: dict):
    title = quote(page["title"])
    url = f'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles={title}'
    data = loads(urlopen(url).read().decode('utf8'))['query']['pages'][page["id"]]['revisions']

    dates = []
    for data, group in groupby(data, lambda info: info['timestamp'].split('T')[0]):
        dates.append([data, len(list(group))])

    return dates


def main():
    pages = [
        {
            'id': '183903',
            'title': 'Градский,_Александр_Борисович',
        },
        {
            'id': '192203',
            'title': 'Бельмондо,_Жан-Поль'
        }
    ]

    print(*get_date(pages[0]), sep='\n')

    print(max(get_date(pages[1]), key=lambda p: p[1]))


if __name__ == '__main__':
    main()