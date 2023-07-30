import tweepy

consumer_key = 'your consumer key'
consumer_secret = 'your secret consumer token'
access_token = 'your access token'
access_token_secret = 'your secret access token'
bearer_token = 'your bearer token'
client_id = 'your client id'
client_secret = 'you client secret key'

client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret,access_token=access_token, access_token_secret=access_token_secret)
user_ids = [2244994945, 6253282]
response = client.get_users(ids=user_ids, user_fields=["profile_image_url"])

for user in response.data:
    print(user.username, user.profile_image_url)