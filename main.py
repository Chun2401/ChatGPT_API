import os
import sys
import time
import openai
import pyttsx3
from colorama import Fore, Back, Style


def setup():
    python = "Hãy cài đặt python để đảm bảo ứng dụng được chạy!\n"
    for a in python:
        sys.stdout.write(a)
        sys.stdout.flush()
        time.sleep(0.02)
    time.sleep(1)

    python2 = "Nhấn CÀI ĐẶT python trong microsoft strore để cài đặt một cách dể dàng!\n"
    for b in python2:
        sys.stdout.write(b)
        sys.stdout.flush()
        time.sleep(0.02)
    time.sleep(2)

    python3 = "Nếu đã cài Python hãy nhập 'exit()'\n"
    for c in python3:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)

    time.sleep(2)
    os.system("python")
    time.sleep(2)
    os.system("pip install --upgrade pip")
    time.sleep(2)
    os.system("pip install openai")
    time.sleep(2)
    os.system("pip install pyttsx3")
    time.sleep(2)

    print("\n-------------------- \n")
    fix_speech = "Nếu bot không nói được tiếng Việt vui lòng xem hết video này và làm theo! https://youtu.be/qVMHoCtjLag?t=847\n"
    for d in fix_speech:
        sys.stdout.write(Fore.RED + d)
        sys.stdout.flush()
        time.sleep(0.02)
    print(Fore.RESET + "\n-------------------- \n")
    time.sleep(5)
    os.system("start https://youtu.be/qVMHoCtjLag?t=847")



engine = pyttsx3.init()

voices = engine.getProperty("voices")
vi_voice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An"
engine.setProperty("voice", vi_voice)
openai.api_key = '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'
engine.connect

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Xin chào"}]
)


def option(String):

    if n == 'lời' or n == 'loi' or n == 'Loi' or n == 'Lời':
        speech()
    elif n == 'chữ' or n == 'Chữ' or n == 'chu' or n == 'Chu':
        reply = completion.choices[0].message.content
        for begin in reply:
            sys.stdout.write(Fore.LIGHTCYAN_EX + begin)
            sys.stdout.flush()
            time.sleep(0.02)
    elif n == 'lời và chữ' or n == 'Lời Và Chữ' or n == 'Loi Va Chu' or n == 'loi va chu':
        reply = completion.choices[0].message.content
        for begin in reply:
            sys.stdout.write(Fore.YELLOW + begin)
            sys.stdout.flush()
            time.sleep(0.02)
        speech()
    else:
        default = "Nếu bạn không chọn, mặc định sẽ là kiểu " + Fore.LIGHTCYAN_EX + "Chữ \n\n"
        for df in default:
            sys.stdout.write(df)
            sys.stdout.flush()
            time.sleep(0.02)
        print(Fore.RESET + "Chọn mặc định: " + Fore.LIGHTCYAN_EX + "Chữ \n\n")

        reply = completion.choices[0].message.content
        for begin in reply:
            sys.stdout.write(Fore.LIGHTCYAN_EX + begin)
            sys.stdout.flush()
            time.sleep(0.02)


def speech():
    print("\n")
    engine.say(completion.choices[0].message.content)
    engine.runAndWait()


# def text():
#     reply = completion.choices[0].message.content

#     for begin in reply:
#         sys.stdout.write(Fore.YELLOW + begin)
#         sys.stdout.flush()
#         time.sleep(0.02)

#     print(Fore.RESET + "\n-----------------------------\n")


error = "Kiểm tra file! (y/N)\n\n"
for a in error:
    sys.stdout.write(a)
    sys.stdout.flush()
    time.sleep(0.02)
input_a = input("Bạn: ")
print(Fore.RESET + "\n-----------------------------\n")

if input_a == "y" or input_a == "Y":
    
    setup()

    select_option = "Bạn muốn AI diễn đạt bằng lời nói hay câu chữ?" + " " + \
        "(" + Fore.CYAN + "lời" + Fore.RESET + " " + "/" + Fore.LIGHTCYAN_EX + " " + "chữ" + \
        Fore.RESET + " " + "/" + Fore.YELLOW + " " + "lời và chữ" + Fore.RESET + ")\n\n"

    for begin in select_option:
        sys.stdout.write(begin)
        sys.stdout.flush()
        time.sleep(0.02)
    n = input(Fore.RESET+"Bạn: ")
    print(Fore.RESET + "\n-----------------------------\n")

    option(n)
    
elif input_a == "N" or input_a == "n":
    select_option = "Bạn muốn AI diễn đạt bằng lời nói hay câu chữ?" + " " + \
        "(" + Fore.CYAN + "lời" + Fore.RESET + " " + "/" + Fore.LIGHTCYAN_EX + " " + "chữ" + \
        Fore.RESET + " " + "/" + Fore.YELLOW + " " + "lời và chữ" + Fore.RESET + ")\n\n"

    for begin in select_option:
        sys.stdout.write(begin)
        sys.stdout.flush()
        time.sleep(0.02)
    n = input(Fore.RESET+"Bạn: ")
    print(Fore.RESET + "\n-----------------------------\n")

    option(n)


while True:
    print(Fore.RESET + "\n-----------------------------\n")
    x = input("Bạn: ")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": x}]
    )
    option(x)
    if x == 'tạm biệt':
        break
