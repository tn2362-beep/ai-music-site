from tkinter import *
from gtts import gTTS
import random
import os

# 단어 데이터
styles = {

    "슬픈": [
        "눈물", "이별", "추억",
        "외로움", "밤", "슬픔"
    ],

    "게임": [
        "전설", "승리", "용기",
        "던전", "모험", "마법"
    ],

    "EDM": [
        "dance", "party", "beat",
        "drop", "music", "fire"
    ],

    "우주": [
        "star", "galaxy", "moon",
        "space", "light", "cosmos"
    ]
}

# AI 생성 함수
def generate_song():

    lyrics_box.delete("1.0", END)

    prompt = input_box.get()

    found_words = []

    # 키워드 분석
    for key in styles:

        if key in prompt:

            found_words += styles[key]

    # 기본 단어
    if len(found_words) == 0:

        found_words = [
            "music",
            "dream",
            "night",
            "light"
        ]

    # 제목
    title = "AI SONG : " + prompt

    lyrics_box.insert(
        END,
        title + "\n\n"
    )

    full_lyrics = ""

    # 가사 생성
    for i in range(8):

        line = ""

        for j in range(6):

            line += random.choice(found_words) + " "

        lyrics_box.insert(
            END,
            line + "\n"
        )

        full_lyrics += line + "\n"

    # AI 음성 생성
    tts = gTTS(
        text=full_lyrics,
        lang='ko'
    )

    tts.save("ai_voice.mp3")

    result_label.config(
        text="AI 음성 MP3 생성 완료!"
    )

    # 자동 실행
    os.system("start ai_voice.mp3")

# 창 생성
window = Tk()

window.title("🤖 AI 노래 생성기")

window.geometry("800x700")

# 제목
title_label = Label(
    window,
    text="🤖 AI 노래 생성기",
    font=("Arial", 28)
)

title_label.pack(pady=20)

# 입력 설명
info_label = Label(
    window,
    text="원하는 음악 분위기를 입력하세요",
    font=("Arial", 14)
)

info_label.pack()

# 입력창
input_box = Entry(
    window,
    width=40,
    font=("Arial", 16)
)

input_box.pack(pady=20)

# 생성 버튼
generate_button = Button(
    window,
    text="🎵 AI 노래 생성",
    font=("Arial", 16),
    width=20,
    height=2,
    command=generate_song
)

generate_button.pack(pady=20)

# 결과 표시
result_label = Label(
    window,
    text="대기 중...",
    font=("Arial", 14)
)

result_label.pack(pady=10)

# 가사 출력창
lyrics_box = Text(
    window,
    width=80,
    height=20,
    font=("Arial", 13)
)

lyrics_box.pack(pady=20)

window.mainloop()