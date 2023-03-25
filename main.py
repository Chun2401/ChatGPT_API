from Setup_file import setup
import os
import sys
import time
import openai
import pyttsx3
from colorama import Fore, Back, Style
from colorama import init, AnsiToWin32
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream


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
        fix_speech = "Nếu bot không nói được tiếng Việt vui lòng xem video này và làm theo! (https://youtu.be/qVMHoCtjLag?t=847)\n"
        for d in fix_speech:
            sys.stdout.write(Fore.RED + d + Fore.RESET)
            sys.stdout.flush()
            time.sleep(0.02)
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

    if "tìm kiếm" in x:
        searchGg = input("\nTìm kiếm: ")
        print("\n")
        for search_value_Gg in searchGg:
            sys.stdout.write(search_value_Gg)
            sys.stdout.flush()
            time.sleep(0.02)
        os.system("start https://www.google.com/search?q=" +
                  searchGg.replace(" ", "+"))
    elif x == "tôi muốn nghe nhạc" or x == "Tôi muốn nghe nhạc":
        searchYt = input("\nBài gì đây: ")
        print("\n")
        for search_value_Yt in searchYt:
            sys.stdout.write(search_value_Yt)
            sys.stdout.flush()
            time.sleep(0.02)
        os.system("start https://www.youtube.com/results?search_query=" +
                  searchYt.replace(" ", "+"))
    else:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": x}]
        )
        option(x)
        if x == 'tạm biệt':
            break
