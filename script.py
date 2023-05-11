import win32gui
import win32process
import keyboard
import os
import signal
import time

shortcut = "ctrl + alt + end"

def getActiveWindowPID():
    if win32gui.GetWindowText(win32gui.GetForegroundWindow()) == "File Explorer":
        return
    else:
        window = win32gui.GetForegroundWindow()
        tid, pid = win32process.GetWindowThreadProcessId(window)
        os.kill(pid, signal.SIGTERM)
        return window

if __name__ == "__main__":
    keyboard.add_hotkey(shortcut, lambda: getActiveWindowPID())
    keyboard.wait()