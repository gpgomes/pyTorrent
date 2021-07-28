import os
from dotenv import load_dotenv


class Configuration(object):
    def __init__(self):
        load_dotenv()

        self.ziped_subtitles_dir = os.getenv('ZIPED_SUBTITLE_DIR')
        self.torrent_dir = os.getenv('TORRENT_DIR')
        self.subtitles_dir = os.getenv('SUBTTITLE_DIR')
        self.external_hd_dir = os.getenv('EXTERNAL_HD_DIR')
        self.utorrent_username = os.getenv('UTORRENT_USERNAME')
        self.utorrent_password = os.getenv('UTORRENT_PASSWORD')