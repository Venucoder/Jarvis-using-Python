import os
import subprocess

paths = {
    'notepad' : "C:\\Windows\\system32\\notepad.exe", 
    'visual studio code' : "C:\\Users\\kalla\\AppData\\Local\\Programs\\'Microsoft VS Code'\\Code.exe", 
    'paint' : "C:\\Windows\\system32\\mspaint.exe", 
    'chrome' : "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    'settings' : "C:\\Windows\\system32\\control.exe", 
    'calculator' : "C:\\Windows\\System32\\calc.exe"
}

def open_notepad():
    os.startfile(paths['notepad'])


def open_vscode():
    os.startfile(paths['visual studio code'])


def open_paint():
    os.startfile(paths['paint'])


def open_chrome():
    os.startfile(paths['chrome'])


def open_settings():
    os.startfile(paths['settings'])


def open_calc():
    os.startfile(paths['calculator'])


def open_cmd():
    os.system('start cmd')


def open_camera():
    subprocess.run('start microsoft.windows.camera:', shell=True)
