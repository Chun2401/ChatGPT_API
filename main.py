import os
import sys
import time
import openai
import pyttsx3
# from tkinter import *

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
os.system("python --version")
time.sleep(2)
os.system("pip install openai")
time.sleep(2)
os.system("pip install pyttsx3")
time.sleep(2)

fix_speech = "Nếu bot không nói được tiếng Việt vui lòng xem hết video này và làm theo! https://youtu.be/qVMHoCtjLag?t=847\n"

for d in fix_speech:
    sys.stdout.write(d)
    sys.stdout.flush()
    time.sleep(0.02)
time.sleep(5)

os.system("start https://youtu.be/qVMHoCtjLag?t=847")


engine = pyttsx3.init()

voices = engine.getProperty("voices")
vi_voice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An"
engine.setProperty("voice", vi_voice)
openai.api_key = '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'


completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Xin chào"}]
)


def option(String):

    if n == 'lời' or n == 'loi' or n == 'Loi' or n == 'Lời':
        speech()
    elif n == 'chữ' or n == 'Chữ' or n == 'chu' or n == 'Chu':
        text()
    elif n == 'lời và chữ' or n == 'Lời Và Chữ' or n == 'Loi Va Chu' or n == 'loi va chu':
        text()
        speech()
    else:
        print("\n\t gặp lỗi...")


def speech():
    engine.say(completion.choices[0].message.content)
    engine.runAndWait()
    print("\n-----------------------------\n")


def text():
    reply = completion.choices[0].message.content

    for begin in reply:
        sys.stdout.write(begin)
        sys.stdout.flush()
        time.sleep(0.02)

    print("\n-----------------------------\n")


select_option = "Bạn muốn AI diễn đạt bằng lời nói hay câu chữ? (lời / chữ / lời và chữ)\n"

for begin in select_option:
    sys.stdout.write(begin)
    sys.stdout.flush()
    time.sleep(0.02)

n = input("Bạn: ")

option(n)

while True:
    x = input("Bạn: ")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": x}]
    )
    option(x)
    if x == 'tạm biệt':
        break
