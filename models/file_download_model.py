from helpers.file_download_helper import download_file_base


class FileDownloadModel:
    def __init__(self, url, file_name=None, directory_name=None):
        self.url = url
        self.file_name = file_name
        self.directory_name = directory_name

    def download(self):
        download_file_base(self.url, self.file_name, self.directory_name)
