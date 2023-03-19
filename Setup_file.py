import os
import sys
import time
from colorama import Fore, Back, Style
# from colorama import init, AnsiToWin32
# init(wrap=False)
# stream = AnsiToWin32(sys.stderr).stream

def setup():
    python = "Hãy cài đặt Python để đảm bảo ứng dụng được chạy!\n\n"
    for a in python:
        sys.stdout.write(a)
        sys.stdout.flush()
        time.sleep(0.02)
    time.sleep(1)

    python2 = "Nhấn CÀI ĐẶT Python trong " + Fore.CYAN + Back.WHITE + "Microsoft Strore"+ Back.RESET +  Fore.RESET + " để cài đặt!\n\n"
    for b in python2:
        sys.stdout.write(b)
        sys.stdout.flush()
        time.sleep(0.02)
    time.sleep(1)

    python3 = "Nếu đã cài Python hãy nhập 'exit()'\n\n"
    for c in python3:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)

    time.sleep(2)
    os.system("python")
    os.system("pip install --upgrade pip")
    os.system("pip install openai")
    os.system("pip install pyttsx3")


    print("\n-------------------- \n")
    fix_speech = "Nếu bot không nói được tiếng Việt vui lòng xem hết video này và làm theo! (https://youtu.be/qVMHoCtjLag?t=847)\n"
    for d in fix_speech:
        sys.stdout.write(Fore.RED + d)
        sys.stdout.flush()
        time.sleep(0.02)
    print(Fore.RESET + "\n-------------------- \n")
    time.sleep(5)
    os.system("start https://youtu.be/qVMHoCtjLag?t=847")
