from textwrap import dedent
from flask import Flask, request
from error_alerts import telegram

alerts = telegram(token='1736901269:AAFD99l-rVHfmPY70huJECgCNnZFCFq5c00', channel=-1001739336908) # @jxdevbot / Blackjack channel

app = Flask(__name__)

@app.route('/sms/', methods=['POST'])
def receive_sms_and_forward():
    '''Receive incoming text messages and forward to Telegram'''
    from_number = request.form['From']
    to_number = request.form['To']
    body = request.form['Body']
    print('Received SMS')
    print()
    message = dedent(f'''\
        From: {from_number}
        To: {to_number}
        Message: {body}
        ''')
    alerts.send_message(message)
    return '<Response></Response>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)