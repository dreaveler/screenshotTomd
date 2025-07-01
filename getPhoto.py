from PIL import Image
import win32clipboard
import io
import time
import base64
import api
class GetPhotoer:
    def __init__(self):
        self.data  = None
        self.hash_num = None
        self.image = None
    def get_clipboard_image(self):
        self.image = Image.open(io.BytesIO(self.data))
    def get_clipboard_checksum(self):
        try:
            win32clipboard.OpenClipboard()
            if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_DIB):
                self.data = win32clipboard.GetClipboardData(win32clipboard.CF_DIB)
                self.hash_num = hash(self.data)
        finally:
            win32clipboard.CloseClipboard()
    def image_to_data_url(self):
        buffered = io.BytesIO()
        self.image.save(buffered, format="PNG")
        base64_image = base64.b64encode(buffered.getvalue()).decode("utf-8")
        return base64_image
    def wait_for_clipboard_image(self):
        last_checksum = self.hash_num
        current_checksum = None
        while True:
            self.get_clipboard_checksum()
            current_checksum = self.hash_num
            if last_checksum != current_checksum and current_checksum is not None:
                self.get_clipboard_image()
                last_checksum = current_checksum
                content = api.ask_moonshot(self.image_to_data_url())
                print(content)
            time.sleep(0.5)
