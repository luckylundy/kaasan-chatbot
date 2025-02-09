from flask import Flask, render_template, request, jsonify
from bot import kaasan_bot

app = Flask(__name__,
    template_folder='../frontend/templates',
    static_folder='../frontend/static'
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json.get('message', '')
    if not user_message:
        return jsonify({'error': 'メッセージが空です'}), 400
    
    # チャットボットからの返答を取得
    bot_response = kaasan_bot(user_message)
    
    return jsonify({
        'response': bot_response
    })

if __name__ == '__main__':
    import os
    port = int(os.getenv("PORT", 8000))  # 環境変数 PORT を使う（デフォルトは 8000）
    app.run(host="0.0.0.0", port=port, debug=True)