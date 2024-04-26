import time
from threading import Thread

import pyperclip

from helpers import file_helper, json_helper


class ClipboardListener(Thread):
    items: list[str] = []

    def __init__(self):
        super(ClipboardListener, self).__init__()
        self.clipboard_data = pyperclip.paste()
        self.running = True

        file_text = file_helper.read_file_as_string("clipboard.json")

        data = json_helper.json_string_to_data(file_text)
        self.items: list[str] = data if data is not None else []

    def run(self):

        try:
            while self.running:
                current_clipboard_data = pyperclip.paste()
                if current_clipboard_data != self.clipboard_data:

                    self.clipboard_data = current_clipboard_data

                    file_text = file_helper.read_file_as_string("clipboard.json")

                    data = json_helper.json_string_to_data(file_text)
                    self.items: list[str] = data if file_text is not None else []

                    current_clipboard_data = "".join(
                        c
                        for c in current_clipboard_data
                        if c not in "\n\r\t\b\f\v\x1b\\"
                    )
                    current_clipboard_data = current_clipboard_data.strip()

                    if current_clipboard_data.isspace() or current_clipboard_data.count(
                        " "
                    ) == len(current_clipboard_data):
                        current_clipboard_data = current_clipboard_data.replace(" ", "")
                    else:
                        current_clipboard_data = "".join(current_clipboard_data.split())

                    if (
                        current_clipboard_data is not None
                        and current_clipboard_data != ""
                        and isinstance(current_clipboard_data, str)
                        and self.items is not None
                        and not self.items.__contains__(current_clipboard_data)
                    ):

                        self.items.append(current_clipboard_data)
                        file_helper.save_string_into_file(
                            json_helper.data_to_json_string(self.items),
                            "clipboard.json",
                        )
                    else:
                        current_clipboard_data = ""

                time.sleep(0.5)

        except Exception as e:
            print(e)

    def stop(self):
        self.running = False


def start_listener():
    listener = ClipboardListener()

    try:
        listener.start()
    except Exception as e:
        print(e)

    print("Clipboard Listener Started.")

    # # Wait for user to press "Q" to exit
    # while True:
    #     key_name = input("Press 'Q' to quit: \n").lower()
    #     if key_name == "q":
    #         listener.stop()
    #         break


# Create a separate thread to start the listener
# listener_thread = Thread(target=start_listener)
# listener_thread.start()

# Main thread can continue with other tasks

# pyinstaller -cF clipboard_listener.py
