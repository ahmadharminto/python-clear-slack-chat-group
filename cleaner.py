import os
from dotenv import load_dotenv
from slack_cleaner2 import *

load_dotenv()

s = SlackCleaner(os.getenv('SLACK_API_TOKEN'))
s.users
s.conversations

'''
delete all messages in channels
for msg in s.msgs(filter(match('.*-bots'), s.conversations)): 
    msg.delete(replies=True, files=True)
'''

if __name__ == '__main__':
    groups = os.getenv('SLACK_GROUPS', '').split(',')
    for group in groups:
        print(f'clearing history chat in group {group} ...')
        for msg in s.msgs(filter(match(group), s.conversations)):
            msg.delete(replies=True, files=True)
