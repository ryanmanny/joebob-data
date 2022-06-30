import json
from pathlib import Path

from bs4 import BeautifulSoup

from util.dates import parse_date_header

SOURCES_PATH = Path('./sources')
MV_HTML_PATH = SOURCES_PATH / '2018_11_08_cinemassacre_monstervision.html'


def compile_monstervision():
    episodes = []

    with open(MV_HTML_PATH) as fp:
        soup = BeautifulSoup(fp, 'html.parser')

    start_header = \
        soup.body.find('h1', text='THE JOE BOB ERA (1996-2000)')

    episode_ps = [
        p for p in start_header.find_all_next('p')
        if p.text.strip()
    ]

    for p in episode_ps:
        if strongs := p.find_all('strong'):
            date_header = "".join(s.text for s in strongs).strip()
            date, note = parse_date_header(date_header)
        else:
            print(p.prettify())
            continue

        episodes.append({
            'date': date.isoformat(),
            'note': note,
        })

    return episodes


def compile():
    data = {
        'monstervision': compile_monstervision(),
    }

    with open('joebob.json', 'w') as fp:
        json.dump(data, fp, indent=2)


if __name__ == '__main__':
    compile()
