from ..settings import DATA_PATHS, SOURCE_URLS
import requests

DEST_PATH = DATA_PATHS['original']
ORIGINAL_URL = SOURCE_URLS['original']


def fetch():
    resp = requests.get(ORIGINAL_URL)
    if resp.status_code == 200:
        return resp.text
    else:
        raise ValueError('Status code was: {}'.format(resp.status_code))


def save(rawtext):
    with open(DEST_PATH, 'w') as w:
        w.write(rawtext)




def fetch_and_save():
    save(fetch())

if __name__ == '__main__':
    print('Fetching', ORIGINAL_URL)
    txt = fetch()
    print("Downloaded", len(txt), 'characters')
    print("Saving to", DEST_PATH)
    save(txt)
