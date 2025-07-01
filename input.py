from pywinauto import Desktop

def input():
    all_windows = Desktop(backend="uia").windows()
    obsidian_windows = [
    w for w in all_windows 
    if "Obsidian" in w.window_text()
    ]
    main_window = obsidian_windows[0]
    main_window.set_focus()
    main_window.type_keys("^V")
    main_window.type_keys("{ENTER}")
    main_window.minimize()