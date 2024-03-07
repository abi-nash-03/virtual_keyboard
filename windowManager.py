import win32gui

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

def get_data():
    results = []
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    # print(top_windows)
    try:
        for i in top_windows:
            if "notepad" in i[1].lower():
                # print(i)
                win32gui.ShowWindow(i[0],5)
                win32gui.SetForegroundWindow(i[0])
                return "notepad"
            elif "brave" in i[1].lower():
                win32gui.ShowWindow(i[0], 5)
                win32gui.SetForegroundWindow(i[0])
                return "brave"
            elif "calculator" in i[1].lower():
                win32gui.ShowWindow(i[0], 5)
                win32gui.SetForegroundWindow(i[0])
                return "calculator"
            # print(i)
    except Exception as ex:
        print("Error during recognition:", ex)

# if __name__ == "__main__":
#     results = []
#     top_windows = []
#     win32gui.EnumWindows(windowEnumerationHandler, top_windows)
#     for i in top_windows:
#         if "brave" in i[1].lower():
#             print(i)
#             win32gui.ShowWindow(i[0],5)
#             win32gui.SetForegroundWindow(i[0])
#             break
#         print(i)