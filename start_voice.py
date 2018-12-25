import os, threading
import subprocess

cmd = ''

def start_browser():
    os.system('espeak "Starting browser"')
    os.system('killall chromium-browser')
    subprocess.Popen(['chromium-browser "hungank.com/devices"'])


while cmd != 'q':
    cmd = input()
    if cmd == 'a':
        start_browser()
    else:
        print(cmd)


