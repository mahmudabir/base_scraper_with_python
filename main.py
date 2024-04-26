import time
from threading import Thread

import constants
from clipboard_listener import start_listener
from helpers.file_helper import download_multiple_file_concurrently, read_file_as_string
from helpers.json_helper import json_string_to_data
from models.file_download_model import FileDownloadModel


def main():
    constants.is_caching_enabled = False

    data = json_string_to_data(read_file_as_string("clipboard.json"))
    data = data if data is not None else []
    is_first_iteration = True

    while True:
        time.sleep(1)
        new_data = json_string_to_data(read_file_as_string("clipboard.json"))
        new_data = new_data if new_data is not None else []

        if is_first_iteration and len(new_data) > 0:
            data = new_data
            files = [FileDownloadModel(x) for x in new_data]
            
            thread = Thread(target=download_multiple_file_concurrently, args=(files,))
            thread.daemon = True
            thread.start()
            
            is_first_iteration = False
        elif data is not None and new_data is not None and new_data != data:
            added_items = list(set(new_data) - set(data)) if data else new_data
            data = new_data
            files = [FileDownloadModel(x) for x in added_items]
            
            thread = Thread(target=download_multiple_file_concurrently, args=(files,))
            thread.daemon = True
            thread.start()


if __name__ == "__main__":
    listener_thread = Thread(target=start_listener)
    listener_thread.start()

    print("Operation Started\n")
    main()
    print("\n\nOperation Completed\n")
