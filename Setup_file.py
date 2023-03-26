
import os
import sys
import time
import pyttsx3
from colorama import Fore, Back, Style

# from colorama import init, AnsiToWin32
# init(wrap=False)
# stream = AnsiToWin32(sys.stderr).stream


def setup():
    check_python = os.system("python --version")
    if check_python == 1:
        python = "Hãy cài đặt Python để đảm bảo ứng dụng được chạy!\n\n"
        for a in python:
            sys.stdout.write(a)
            sys.stdout.flush()
            time.sleep(0.02)
        os.system(
            "start https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe")
        time.sleep(60)
        os.system("pip install --upgrade pip")
        os.system("pip install openai")
        os.system("pip install pyttsx3")
        os.system("exit")
    else:
        os.system("pip install --upgrade pip")
        os.system("pip install openai")
        os.system("pip install pyttsx3")

        Check_Speech = "Kiểm tra giọng nói của AI...!\n\n"
        for speech in Check_Speech:
            sys.stdout.write(speech)
            sys.stdout.flush()
            time.sleep(0.02)
        engine.say("Xin chào! tôi là AI của OpenAI.")

        print("\n-------------------- \n")
        fix_speech = "Nếu bot không nói được tiếng Việt vui lòng xem video này và làm theo! (https://youtu.be/qVMHoCtjLag?t=847)\n"
        for d in fix_speech:
            sys.stdout.write(Fore.RED + d)
            sys.stdout.flush()
            time.sleep(0.02)
        print(Fore.RESET + "\n-------------------- \n")
        time.sleep(3)
        os.system("python main.py")
