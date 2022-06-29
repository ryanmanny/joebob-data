import json
from pathlib import Path

from bs4 import BeautifulSoup

SOURCES_PATH = Path('./sources')
MONSTERVISION_HTML_PATH = SOURCES_PATH / '2018_11_08_cinemassacre_monstervision.html'


def compile_monstervision():
    with open(MONSTERVISION_HTML_PATH) as fp:
        soup = BeautifulSoup(fp, 'html.parser')

    raise NotImplementedError()


def compile():
    data = {
        'monstervision': compile_monstervision(),
    }

    with open('joebob.json', 'w') as fp:
        json.dump(data, fp)


if __name__ == '__main__':
    compile()