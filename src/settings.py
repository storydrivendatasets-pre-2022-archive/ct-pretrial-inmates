from pathlib import Path
DATA_DIR = Path('data')

DATA_PATHS = {
    'original': DATA_DIR.joinpath('original', 'records.csv')
}

SOURCE_URLS = {
    'original': 'https://data.ct.gov/api/views/b674-jy6w/rows.csv?accessType=DOWNLOAD'
}



def setup():
    RAW_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
