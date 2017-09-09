from slackclient import SlackClient

#slack_client = SlackClient('xoxp-87030285349-87039528343-173762986482-e7badabfe0e4b37e9c30c3f294a9af08')
slack_client = SlackClient('xoxp-87030285349-87039528343-173089390704-5c13f07dbca43ccae65088ce7a888912')
a = slack_client.api_call("api.test")

print a


def list_channels():
    #slack_client = SlackClient('xoxp-87030285349-87039528343-173762986482-e7badabfe0e4b37e9c30c3f294a9af08')
    slack_client = SlackClient('xoxp-87030285349-87039528343-173089390704-5c13f07dbca43ccae65088ce7a888912')
    channels_call = slack_client.api_call("channels.list")
    if channels_call.get('ok'):
        return channels_call['channels']
    return None

def channel_info(channel_id):
    channel_info = slack_client.api_call("channels.info", channel=channel_id)
    if channel_info:
        return channel_info['channel']
    return None

def send_message(channel_id, message):
    #slack_client = SlackClient('xoxp-87030285349-87039528343-173762986482-e7badabfe0e4b37e9c30c3f294a9af08')
    slack_client = SlackClient('xoxp-87030285349-87039528343-173089390704-5c13f07dbca43ccae65088ce7a888912')
    slack_client.api_call(
        "chat.postMessage",
        channel=channel_id,
        text=message,
        username='TCB',
        icon_emoji=':robot_face:'
    )

def send_to_channel(channel_name,messege):
    channels = list_channels()
    if channels:
        for channel in channels:
            if channel['name'] == channel_name:
                print ("send")
                send_message(channel['id'], messege )

        print('-----')
    else:
        print("Unable to authenticate.")


if __name__ == '__main__':
    channels = list_channels()
    if channels:
        for channel in channels:
            print(channel['name'] + " (" + channel['id'] + ")")
            detailed_info = channel_info(channel['id'])
            if detailed_info:
                print('Latest text from ' + channel['name'] + ":")
                print(detailed_info['latest']['text'])
            if channel['name'] == 'ask-tcb!':
                send_message(channel['id'], "Hello " +
                             channel['name'] + "! It worked!")

        print('-----')
    else:
        print("Unable to authenticate.")



