
# def enum_windows_callback(hwnd, extra):
#     # Check if the window is visible and has a title
#     if win32gui.IsWindowVisible(hwnd):
#         title = win32gui.GetWindowText(hwnd)
#         if title:
#             print(f"Window Handle: {hwnd} | Title: {title}")
#     return True  # Return True to continue enumeration
#
# # Call the function
# win32gui.EnumWindows(enum_windows_callback, None)

import win32clipboard
import win32con
import time

copiedList = []

while True:
    opened = False

    try:
        win32clipboard.OpenClipboard()
        opened = True

        if win32clipboard.IsClipboardFormatAvailable(
            win32con.CF_UNICODETEXT
        ):
            copied = win32clipboard.GetClipboardData(
                win32con.CF_UNICODETEXT
            )

            if copied not in copiedList:
                copiedList.append(copied)
                print("\n".join(copiedList))
                print("-" * 30)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if opened:
            win32clipboard.CloseClipboard()

    time.sleep(0.5)

