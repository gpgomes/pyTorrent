from os import path
from utils.configuration import Configuration
from handlers.file_handler import FileHandler


class Torrent(object):

    def __init__(self, subtitle):
        self.configuration = Configuration()
        self.file_handler = FileHandler()
        self.title = subtitle[0:len(subtitle)-4]
        self.subtitle = subtitle
        self.subtitle_path = self.set_subtitle_path()
        self.magnet_link = ''
        self.directory = ''
        self.video_file = ''
        self.video_path = ''
        self.ready = False
        self.done = False

    def set_magnet_link(self, magnet_link: str):
        self.magnet_link = magnet_link

    def set_subtitle_path(self):
        return path.join(self.configuration.subtitles_dir, self.subtitle)

    def set_directory(self, directory_list):
        for directory in directory_list:
            if self.title in directory:
                self.directory = path.join(self.configuration.torrent_dir, directory)

    def set_video_path(self):
        video_files = self.file_handler.search_video_files(directory=self.directory)
        if len(video_files) > 0:
            self.video_path = path.join(self.directory, video_files[0])
            self.video_file = video_files[0]
            if self.video_file != '':
                self.ready = True

    def move_to_hd_dir(self):
        if self.ready:
            new_video_path = path.join(self.configuration.external_hd_dir, self.video_file)
            new_subtitle_path = path.join(self.configuration.external_hd_dir, self.subtitle)
            self.file_handler.move_files(src=self.video_path, dst=new_video_path)
            self.file_handler.move_files(src=self.subtitle_path, dst=new_subtitle_path)
            self.done = True
