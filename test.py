import os
import os
import sys
import time
from colorama import Fore, Back, Style

check_python = os.system("python --version")
if check_python == 0:
    python = "Hãy cài đặt Python để đảm bảo ứng dụng được chạy!\n\n"
    for a in python:
        sys.stdout.write(a)
        sys.stdout.flush()
        time.sleep(0.02)
    time.sleep(1)
    os.system(
        "start https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe")
else:
    print("ok")
