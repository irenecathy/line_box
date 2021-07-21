from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('rIpECsbAOs1XJ1mB1BwpG+xkPFGIijRs6Hv6SGn0AMCZ0pff03MIGSjBoJRvk7paqJemTzKO6SO3AWwrLGR+k645zolFgk8dwbBz4cHjeTRgYyMxi2pTGf9QXkjaEq9wkR0Z+4n02CJXYk5A8bPo7gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('e1a3a69b60718ffc007456560d34d77f')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '我看不懂你說什麼'

    if '貼圖' in msg:
        sticker_message = StickerSendMessage(
            package_id='1',
            sticker_id='1'
        )

        line_bot_api.reply_message(
            event.reply_token,
            sticker_message)

        return #function 遇到return 就會結束掉


    if msg in ['hi', 'Hi'] :
        r = ''
    elif msg == '你吃飯了嗎':
        r = '還沒'
    elif msg == '你是誰':
        r = '我是機器人'
    elif '訂位' in msg:
        r = '您想訂位，是嗎？' 


    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()
