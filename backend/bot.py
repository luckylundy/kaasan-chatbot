import random
import os
from dotenv import load_dotenv
from openai import OpenAI

# 環境変数を読み込む
load_dotenv()

def kaasan_bot(ユーザーの質問):
    # テスト用の返答リスト
    responses = [
        "あんた、そないに落ち込まんでもええよ。明日はきっといい日になるわ！",
        "そないな時もあるわな。でも、あんたなら乗り越えられる！",
        "辛いときは辛いって言っていいんやで。母さんが聞いとるから。",
        "あんた、よう頑張ってるやないの。もっと自分を褒めてあげな！",
        "そない思うのも当たり前や。でも、あんたには良いところがいっぱいあるんやで！"
    ]
    return random.choice(responses)

# OpenAI APIを使用する場合のコード（現在はコメントアウト）
"""
def kaasan_bot_with_api(ユーザーの質問):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "system",
            "content": "あなたは大阪弁で話す、温かく励ましてくれる肝っ玉母さんです。相手を「あんた」と呼び、いつも前向きで力強い言葉をかけてくれます。"
        }, {
            "role": "user",
            "content": ユーザーの質問
        }])
    return response.choices[0].message.content
"""