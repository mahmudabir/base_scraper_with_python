

import constants
from helpers.file_helper import FileDownloadModel, download_multiple_file_concurrently


def main():
    constants.is_caching_enabled = False
    
    files = [
        FileDownloadModel("http://10.16.100.214/iccftps14/iccftps14sasd5/Tv%20Show/Serials%20(Animation)/I%20Am%20Groot%20Season%2002%20(2023)%20Completed/I%20Am%20Groot%20S02E01.mp4"),
        FileDownloadModel("http://10.16.100.214/iccftps14/iccftps14sasd5/Tv%20Show/Serials%20(Animation)/I%20Am%20Groot%20Season%2002%20(2023)%20Completed/I%20Am%20Groot%20S02E02.mp4"),
        FileDownloadModel("http://10.16.100.214/iccftps14/iccftps14sasd5/Tv%20Show/Serials%20(Animation)/I%20Am%20Groot%20Season%2002%20(2023)%20Completed/I%20Am%20Groot%20S02E03.mp4"),
        FileDownloadModel("http://10.16.100.214/iccftps14/iccftps14sasd5/Tv%20Show/Serials%20(Animation)/I%20Am%20Groot%20Season%2002%20(2023)%20Completed/I%20Am%20Groot%20S02E04.mp4"),
        FileDownloadModel("http://10.16.100.214/iccftps14/iccftps14sasd5/Tv%20Show/Serials%20(Animation)/I%20Am%20Groot%20Season%2002%20(2023)%20Completed/I%20Am%20Groot%20S02E05.mp4"),
        FileDownloadModel("https://mcbuild.org/static/images/items/5/e00af2f0691_mcbuild.webp"),
        FileDownloadModel("https://mcbuild.org/static/images/items/12/ed55b223418_mcbuild.webp"),
        FileDownloadModel("https://mcbuild.org/static/images/items/12/ff16dc90571_mcbuild.webp"),
        FileDownloadModel("https://mcbuild.org/static/images/items/12/53ee5161677_mcbuild.webp"),
    ]

    download_multiple_file_concurrently(files)


if __name__ == "__main__":
    print("Operation Started\n")
    main()
    print("\n\nOperation Completed\n")
