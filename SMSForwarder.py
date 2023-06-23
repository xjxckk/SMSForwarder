from textwrap import dedent
from flask import Flask, request, redirect
from error_alerts import telegram

alerts = telegram(token='1736901269:AAFD99l-rVHfmPY70huJECgCNnZFCFq5c00') # @jxdevbot

syndicate_channel = -920168991 # 'Blackjack' channel
'''
Syndicate numbers (https://dev.jxck.ml/sms-forwarder/syndicate/):
+39 339 990 8320
'''
tristzan_channel = -965988103 # 'SMS forwarding' channel
'''
Tristzan numbers (https://dev.jxck.ml/sms-forwarder/tristzan/):
+39 339 995 8629
'''

app = Flask(__name__)

@app.route('/')
def redirect_to_main_site():
    return redirect('https://jxck.ml')

@app.route('/<client>/', methods=['GET', 'POST'])
def receive_sms_and_forward(client):
    if request.method == 'POST':
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

        if client == 'tristzan':
            alerts.send_message(message, channel=tristzan_channel)
        elif client == 'syndicate':
            alerts.send_message(message, channel=syndicate_channel)
        return '<Response></Response>'

    else:
        return redirect_to_main_site()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)