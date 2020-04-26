from AppKit import NSWorkspace
import time

open_window = ""

while True:
        new_window = (NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName'])

        if open_window != new_window:
                open_window = new_window
                print(open_window)
        
        time.sleep(10)