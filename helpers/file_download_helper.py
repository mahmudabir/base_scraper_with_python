import os
import time
from urllib.parse import unquote

import requests

from helpers.app_constants import Color


def download_file_base(url, file_name=None, directory_name=None):
    """
    Downloads a file from the given URL and saves it to the specified directory with the given file name.

    Args:
        url (str): The URL of the file to download.
        file_name (str, optional): The name of the file to save. If not provided, the file name will be extracted from the URL. Defaults to None.
        directory_name (str, optional): The name of the directory to save the file in. If not provided, the file will be saved in a directory named "downloads". Defaults to None.

    Returns:
        None

    Raises:
        None
    """

    try:
        response = requests.get(url, timeout=5, stream=True)
        total_length = int(response.headers.get("content-length", 0))
        directory_name = "downloads" if directory_name is None else directory_name
        file_name = os.path.basename(unquote(url)) if file_name is None else file_name

        os.makedirs(directory_name, exist_ok=True)
        full_file_path = os.path.join(directory_name, file_name)

        with open(full_file_path, "wb") as f:
            dl = 0
            start_time = time.time()
            update_time = start_time

            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                elapsed_time = time.time() - start_time
                download_speed = dl / (1024 * elapsed_time) if elapsed_time > 0 else 0
                percent_done = dl / total_length * 50 if total_length > 0 else 0

                if time.time() - update_time >= 2:
                    progress_bar_completed = "=" * int(percent_done / 2)
                    progress_bar_remaining = " " * (25 - int(percent_done / 2))
                    downloaded_size = dl / (1024 * 1024)
                    file_size = total_length / (1024 * 1024)
                    print(
                        f"""{Color.PURPLE}Downloading \"{file_name}\": [{progress_bar_completed}{progress_bar_remaining}] {Color.BLUE}[Progress: {percent_done:.2f}%] {Color.GREEN}[Speed: {download_speed:.3f} KB/s] {Color.YELLOW}[{downloaded_size:.2f} MB / {Color.RED}{file_size:.2f} MB] {Color.RESET}\r""",
                        end="\r",
                    )

                    update_time = time.time()

        print("Download complete!")
        print(
            f'File: "{Color.GREEN}{os.path.dirname(os.path.abspath(__file__))}\\{full_file_path}{Color.RESET}"'
        )
    except Exception as ex:
        # raise ex
        print(ex.with_traceback(ex.__traceback__))
