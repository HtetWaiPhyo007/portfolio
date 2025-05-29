from flask import Flask, render_template, jsonify, request
import random
import datetime

app = Flask(__name__)

# ラッキーカラーとナンバーのリスト
lucky_colors = ["赤", "青", "緑", "黄色", "紫", "オレンジ", "ピンク"]

def get_lucky_color(name, birthday):
    return lucky_colors[sum(ord(c) for c in name + birthday) % len(lucky_colors)]

def get_lucky_number(name, birthday):
    return (sum(ord(c) for c in name + birthday) % 99) + 1

def get_zodiac_sign(birthday):
    month, day = map(int, birthday.split('-')[1:])
    zodiac_signs = {
        (3, 21): "牡羊座", (4, 20): "牡牛座", (5, 21): "双子座", (6, 21): "蟹座", (7, 23): "獅子座",
        (8, 23): "乙女座", (9, 23): "天秤座", (10, 23): "蠍座", (11, 22): "射手座", (12, 22): "山羊座",
        (1, 20): "水瓶座", (2, 19): "魚座"
    }
    for (m, d), sign in reversed(zodiac_signs.items()):
        if (month, day) >= (m, d):
            return sign
    return "魚座"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/lucky')
def lucky():
    name = request.args.get("name", "不明")
    birthday = request.args.get("birthday", "0000-00-00")
    color = get_lucky_color(name, birthday)
    number = get_lucky_number(name, birthday)
    return jsonify({"color": color, "number": number})

@app.route('/compatibility')
def compatibility():
    name1 = request.args.get("name1", "不明")
    name2 = request.args.get("name2", "不明")
    score = random.randint(40, 100)
    fortune_messages = [
        "強くて冒険的な絆が待っています！",
        "あなたたちは完璧に補い合っています！",
        "困難が来るかもしれませんが、愛が勝ちます！",
        "一緒にいることでワクワクする未来が待っています！",
        "あなたたちの関係はポジティブなエネルギーに満ちています！"
    ]
    fortune = random.choice(fortune_messages)
    return jsonify({"score": score, "fortune": fortune})

@app.route('/horoscope')
def horoscope():
    return render_template('horoscope.html')

@app.route('/get_horoscope')
def get_horoscope():
    birthday = request.args.get("birthday", "0000-00-00")
    zodiac = get_zodiac_sign(birthday)
    horoscope_messages = {
        "牡羊座": "エネルギッシュな一日になりそう！",
        "牡牛座": "落ち着いて行動すると良い結果に繋がります。",
        "双子座": "新しい出会いが期待できるかも！",
        "蟹座": "家族や友人との時間を大切にしましょう。",
        "獅子座": "リーダーシップを発揮するチャンス！",
        "乙女座": "細かい部分に注意を払うと成功に繋がります。",
        "天秤座": "バランスの取れた一日を心がけましょう。",
        "蠍座": "情熱を持って取り組むと良いことが起こるでしょう。",
        "射手座": "冒険心を持って新しいことに挑戦してみましょう。",
        "山羊座": "計画を立てることで目標達成が早まります。",
        "水瓶座": "独創的なアイデアが成功の鍵になります。",
        "魚座": "直感を信じて行動すると良いでしょう。"
    }
    return jsonify({"horoscope": horoscope_messages.get(zodiac, "今日の運勢は予測できません。")})

@app.route('/lucky-compatibility')
def lucky_compatibility():
    return render_template('lucky_compatibility.html')

if __name__ == '__main__':
    app.run(debug=True)
