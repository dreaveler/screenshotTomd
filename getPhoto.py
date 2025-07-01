from PIL import Image
import win32clipboard
import io
def get_clipboard_image():
    win32clipboard.OpenClipboard()
    try:
        if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_DIB):
            # 获取位图数据
            data = win32clipboard.GetClipboardData(win32clipboard.CF_DIB)
            # 转换为 PIL Image
            image = Image.open(io.BytesIO(data))
        else:
            pass
    finally:
        win32clipboard.CloseClipboard()
    return None
def check_new_image():
    win32clipboard.OpenClipboard()