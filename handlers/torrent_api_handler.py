import requests
from time import sleep

from utils.audit import Audit


class TorrentAPIHandler(object):

    def __init__(self):
        self.audit = Audit(type(self).__name__)
        self.headers = {'User-Agent': 'curl/7.37.0'}
        self.token = ''
        self.get_token()

    def get_token(self):

        token_request_url = 'https://torrentapi.org/pubapi_v2.php?get_token=get_token&app_id=NodeTorrentSearchApi'
        try:
            request = requests.get(url=token_request_url, headers=self.headers)
            self.token = request.json()['token']
            self.audit.info('Token OK')
        except:
            self.audit.error("Error getting token")

    def get_search_url(self, query):
        main_url = 'https://torrentapi.org/pubapi_v2.php?app_id=NodeTorrentSearchApi&'
        category = '1;4;14;15;16;17;21;22;42;18;19;41;27;28;29;30;31;' \
                   '32;40;23;24;25;26;33;34;43;44;45;46;47;48;49;50;51;52'
        search_url = f'{main_url}search_string={query}&category={category}&mode=search&format=json_extended&' \
                     f'sort=seeders&limit=4&token={self.token}'
        return search_url

    def make_request(self, search_url):
        request = requests.get(url=search_url, headers=self.headers)
        if request.status_code != 200:
            raise Exception(f'Status Code {request.status_code}')

        request_json = request.json()

        if 'error' in request_json.keys():
            return False
        else:
            torrent_result = request_json['torrent_results'][0]
            self.audit.info(f"{torrent_result['title']} - OK")
            return torrent_result['download']

    def get_magnet_link(self, query, retry=3):
        self.audit.info(f"Searching {query}")
        search_url = self.get_search_url(query=query)
        if retry > 0:
            try:
                result = self.make_request(search_url=search_url)
                if not result:
                    self.audit.warning("Waiting...")
                    sleep(10)
                    self.audit.warning(f"Retry number {retry}")
                    self.get_magnet_link(query=query, retry=retry-1)
                else:
                    return result

            except Exception as E:
                self.audit.error(f'Error getting magnet_link for {query}: {E}')
        else:
            self.audit.error(f'No more tries for {query}')
            self.audit.error(f'Error getting magnet_link for {query}')
