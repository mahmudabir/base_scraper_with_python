
import constants
from helpers.file_helper import download_multiple_file_concurrently, read_file_as_string
from helpers.json_helper import json_string_to_data
from models.file_download_model import FileDownloadModel


def main():
    constants.is_caching_enabled = False
    
    data = json_string_to_data(read_file_as_string("clipboard.json"))
    files = [FileDownloadModel(x) for x in data]
    download_multiple_file_concurrently(files)


if __name__ == "__main__":
    print("Operation Started\n")
    main()
    print("\n\nOperation Completed\n")
