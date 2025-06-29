import tweepy

BEARER_TOKEN = 'bearer_token_anda'

client = tweepy.Client (bearer_token=BEARER_TOKEN)

#mencari tweet baru dengan kata kunci "freya" max:10
response = client.search_recent_tweets(query='freya', max_results=10)

#menampilkan tweet yang ditemukan
if response.data:
    for tweet in response.data:
        print(tweet.text)
else:
    print("Tidak ada tweet yang ditemukan")