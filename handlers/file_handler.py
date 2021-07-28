from utils.configuration import Configuration
from os import walk, path
import zipfile
import shutil
import ntpath


class FileHandler(object):

    def __init__(self):
        self.configuration = Configuration()

    def search_subtitles(self):
        return self.search_files(directory=self.configuration.subtitles_dir, file_extension='.srt')

    def search_zip_files(self):
        return self.search_files(directory=self.configuration.ziped_subtitles_dir, file_extension='.zip')

    def search_video_files(self, directory):
        video_list = self.search_files(directory=directory, file_extension='.mkv')
        if len(video_list) == 0:
            video_list = self.search_files(directory=directory, file_extension='.mp4')
        return video_list

    @staticmethod
    def search_files(directory: str, file_extension: str) -> list:
        file_names = []
        for (dirpath, dirnames, filenames) in walk(directory):
            for file in filenames:
                if file.endswith(file_extension):
                    file_names.append(file)
        return file_names

    @staticmethod
    def path_leaf(path):
        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)

    def unzip_files(self, file_name: str) -> bool:
        try:
            path_to_zip_file = path.join(path.join(self.configuration.ziped_subtitles_dir, file_name))
            zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
            zip_ref.extractall(self.configuration.subtitles_dir)
            for unziped_file in zip_ref.filelist:
                file_path = unziped_file.filename
                file_dir = path.dirname(file_path)
                file_name = self.path_leaf(unziped_file.filename)
                if path.splitext(file_name)[1] == '.srt':
                    shutil.move(
                        src=path.join(self.configuration.subtitles_dir, file_path),
                        dst=path.join(self.configuration.subtitles_dir, file_name)
                    )
            zip_ref.close()
            shutil.rmtree(path.join(self.configuration.subtitles_dir, file_dir))
        except Exception as e:
            print(e)
            return False

    def get_subdiretories(self):
        subdirectories = []
        for (dirpath, dirnames, filenames) in walk(self.configuration.torrent_dir):
            for subdirectory in dirnames:
                subdirectories.append(subdirectory)
        return subdirectories

    @staticmethod
    def move_files(src, dst):
        shutil.move(src=src, dst=dst)

