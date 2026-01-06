from dotenv import load_dotenv
import os

#呼叫dotenv
load_dotenv()

channel_access_token = os.getenv('channel_access_token')
channel_secret = os.getenv('channel_secret')

print(channel_access_token)
print(channel_secret)
