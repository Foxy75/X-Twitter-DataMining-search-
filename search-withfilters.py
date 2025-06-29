import tweepy

BEARER_TOKEN = 'token_bearer_anda'

client = tweepy.Client (bearer_token=BEARER_TOKEN)
# contoh:tweet yang mengandung kata kunci "freya" dan bukan retweet
query = 'from:freya -is:retweet'

#from:username
#@mention
#has:links

#mencari tweet baru dengan kata kunci 
response = client.search_recent_tweets(query=query, max_results=10)

#menampilkan tweet yang ditemukan
if response.data:
    for tweet in response.data:
        print(tweet.text)
else:
    print("Tidak ada tweet yang ditemukan")