from utils.configuration import Configuration
from handlers.torrent_api_handler import TorrentAPIHandler
from handlers.file_handler import FileHandler
from handlers.utorrent_api_handler import UTorrentAPI
from utils.audit import Audit
from torrent import Torrent


class PyTorrent(object):
    def __init__(self):
        self.configuration = Configuration()
        self.torrentAPIHandler = TorrentAPIHandler()
        self.file_handler = FileHandler()
        self.audit = Audit(type(self).__name__)
        self.torrent_list = []
        self.utorrent_client = None

    def get_subtitles(self):
        for zip_file in self.file_handler.search_zip_files():
            self.file_handler.unzip_files(zip_file)

    def get_subtitles_to_search(self):
        for subtitle in self.file_handler.search_subtitles():
            new_torrent = Torrent(subtitle=subtitle)
            self.torrent_list.append(new_torrent)

    def get_torrents(self):
        for torrent in self.torrent_list:
            magnet_link = self.torrentAPIHandler.get_magnet_link(query=torrent.title)
            self.utorrent_client.add_url(magnet_link)

    def setting_files(self):
        subdirectories_list = self.file_handler.get_subdiretories()
        for torrent in self.torrent_list:
            torrent.set_directory(directory_list=subdirectories_list)
            torrent.set_video_path()
            torrent.move_to_hd_dir()
            if torrent.done:
                self.audit.info(msg="%s moved" % torrent.title)

    def execute(self):
        self.audit.info("Starting")
        self.utorrent_client = UTorrentAPI('http://127.0.0.1:8080/gui', self.configuration.utorrent_username,
                                           self.configuration.utorrent_password)
        self.audit.input("Give me a number: ")
        option = int(input())

        if option == 0:
            self.audit.info("Extracting subtitles")
            self.get_subtitles()
        elif option == 1:
            self.audit.info("Get Magnet Links")
            self.get_subtitles_to_search()
            self.get_torrents()
        elif option == 2:
            self.get_subtitles_to_search()
            self.audit.info("Setting files")
            self.setting_files()
        else:
            pass
        self.audit.info("Finished")


if __name__ == '__main__':
    pyTorrent = PyTorrent()
    pyTorrent.execute()
