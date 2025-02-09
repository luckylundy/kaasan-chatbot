import os
from dotenv import load_dotenv
from openai import OpenAI
import random

# 環境変数を読み込む
load_dotenv()

# クライアントの初期化
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# def kaasan_bot(ユーザーの質問):
#     # 肝っ玉母さんの返答を生成
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[{
#             "role":
#             "system",
#             "content":
#             "あなたは大阪弁で話す、温かく励ましてくれる肝っ玉母さんです。相手を「あんた」と呼び、いつも前向きで力強い言葉をかけてくれます。"
#         }, {
#             "role": "user",
#             "content": ユーザーの質問
#         }])
#     return response.choices[0].message.content


def kaasan_bot(ユーザーの質問):
    # テスト用の返答リスト
    responses = [
        "あんた、そないに落ち込まんでもええよ。明日はきっといい日になるわ！", "そないな時もあるわな。でも、あんたなら乗り越えられる！",
        "辛いときは辛いって言っていいんやで。母さんが聞いとるから。", "あんた、よう頑張ってるやないの。もっと自分を褒めてあげな！",
        "そない思うのも当たり前や。でも、あんたには良いところがいっぱいあるんやで！"
    ]
    return random.choice(responses)


# 会話ループ
def main():
    print("肝っ玉母さん: あんた、何か悩みがあるんやったら何でも言うてみぃ！")

    while True:
        user_input = input("あなた: ")
        if user_input.lower() == 'bye':
            print("肝っ玉母さん: ほな、また来てな！")
            break

        response = kaasan_bot(user_input)
        print(f"肝っ玉母さん: {response}")


if __name__ == "__main__":
    main()
