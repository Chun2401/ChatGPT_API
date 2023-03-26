
import os
import sys
import time
import openai
from colorama import Fore, Back, Style
from colorama import init, AnsiToWin32
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream

print("\n\n")

chun = (" ▄████▄   ██░ ██  █    ██  ███▄    █ \n") + \
    ("▒██▀ ▀█  ▓██░ ██▒ ██  ▓██▒ ██ ▀█   █ \n") + \
    ("▒▓█    ▄ ▒██▀▀██░▓██  ▒██░▓██  ▀█ ██▒\n") + \
    ("▒▓▓▄ ▄██▒░▓█ ░██ ▓▓█  ░██░▓██▒  ▐▌██▒\n") + \
    ("▒ ▓███▀ ░░▓█▒░██▓▒▒█████▓ ▒██░   ▓██░\n") + \
    ("░ ░▒ ▒  ░ ▒ ░░▒░▒░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ \n") + \
    ("  ░  ▒    ▒ ░▒░ ░░░▒░ ░ ░ ░ ░░   ░ ▒░\n") + \
    ("  ░  ▒    ▒ ░▒░ ░░░▒░ ░ ░ ░ ░░   ░ ▒░\n") + \
    ("░ ░       ░  ░  ░   ░              ░ \n") + \
    ("░") +\
    ("\n\n")


for ten in chun:
    sys.stdout.writelines(Fore.YELLOW + ten)
    # sys.stdout.flush()
    # time.sleep(0.01)

key_api = input(Fore.RESET + "Hãy nhập Key api của bạn ở đây: ")
openai.api_key = key_api

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Xin chào"}]
)

print("\n")
reply = completion.choices[0].message.content
for begin in reply:
    sys.stdout.write(Fore.YELLOW + begin)
    sys.stdout.flush()
    time.sleep(0.02)


def speech():
    print("\n")
    engine.say(completion.choices[0].message.content)
    engine.runAndWait()


def text(String):
    reply = completion.choices[0].message.content

    for begin in reply:
        sys.stdout.write(Fore.YELLOW + begin)
        sys.stdout.flush()
        time.sleep(0.02)


while True:

    print(Fore.RESET + "\n-----------------------------\n")
    x = input("Bạn: ")

    if "tìm kiếm" in x:
        searchGg = input("\nTìm kiếm: ")
        print("\n")
        for search_value_Gg in searchGg:
            sys.stdout.write(Fore.YELLOW + search_value_Gg)
            sys.stdout.flush()
            time.sleep(0.02)
        os.system("start https://www.google.com/search?q=" +
                  searchGg.replace(" ", "+"))
    elif x == "tôi muốn nghe nhạc" or x == "Tôi muốn nghe nhạc":
        searchYt = input("\nBài gì đây: ")
        print("\n")
        for search_value_Yt in searchYt:
            sys.stdout.write(Fore.YELLOW + search_value_Yt)
            sys.stdout.flush()
            time.sleep(0.02)
        os.system("start https://www.youtube.com/results?search_query=" +
                  searchYt.replace(" ", "+"))
    else:
        print("\n")
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": x}]
        )
        text(x)
        if x == 'tạm biệt':
            time.sleep(2)
            break
