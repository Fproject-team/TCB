from flask import Flask, request, Response
from classifyTest import classify
#from classifyTestDBOrganize import classify
from app import send_to_channel

app = Flask(__name__)

#SLACK_WEBHOOK_SECRET = '7GWfBofDJWeGTIi4jPY7Cwdf'
SLACK_WEBHOOK_SECRET = 'aBs7oz3QFZ7pJrQQFlaicdgt'


@app.route('/slack', methods=['POST'])
def inbound():
    if request.form.get('token') == SLACK_WEBHOOK_SECRET:
        channel = request.form.get('channel_name')
        print channel
        username = request.form.get('user_name')
        print username
        text = request.form.get('text')
        print text
        inbound_message = username + " in " + channel + " says: " + text
        print inbound_message
        category =  classify(text)
        outbound_message = "A ticket is opened to the " + category + " department"
        print outbound_message
        send_to_channel(channel,outbound_message)
        print(inbound_message)
    return Response(), 200


@app.route('/', methods=['GET'])
def test():
    return Response('It works!')

if __name__ == "__main__":
    app.run(debug=True)