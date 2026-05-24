from flask import Flask, request
import random

app = Flask(__name__)

# 스타일 단어
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

# 메인 페이지
@app.route("/", methods=["GET", "POST"])

def home():

    lyrics = ""

    if request.method == "POST":

        prompt = request.form["prompt"]

        found_words = []

        # 단어 찾기
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
        lyrics += f"🎵 {prompt}<br><br>"

        # 가사 생성
        for i in range(8):

            line = ""

            for j in range(6):

                line += random.choice(found_words) + " "

            lyrics += line + "<br><br>"

    return f"""

    <html>

    <head>

        <title>AI 음악 생성기</title>

    </head>

    <body style="
        background:black;
        color:white;
        font-family:Arial;
        text-align:center;
        padding-top:50px;
    ">

        <h1>🎵 AI 음악 생성기</h1>

        <form method="POST">

            <input
                name="prompt"
                style="
                    width:400px;
                    padding:15px;
                    font-size:20px;
                "
                placeholder="예: 슬픈 우주 음악"
            >

            <br><br>

            <button
                style="
                    padding:15px;
                    font-size:20px;
                "
            >
                🎵 생성하기
            </button>

        </form>

        <div style="
            margin-top:50px;
            font-size:24px;
        ">

            {lyrics}

        </div>

    </body>

    </html>
    """

app.run(host="0.0.0.0", port=10000)