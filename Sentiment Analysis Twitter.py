
# coding: utf-8

# In[1]:


import tweepy
from textblob import TextBlob 
import pandas as pd


# In[2]:


consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''


# In[3]:


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


# In[4]:


api = tweepy.API(auth)


# In[45]:


number_of_tweets=200
public_tweet = api.user_timeline(screen_name='DeadlineDayLive')

twitter = list()
for tweet in public_tweet:
    analysis = TextBlob(tweet.text)
    sentimen = analysis.sentiment
    if sentimen.polarity > 0.0:
        emosi = "Positive"
    elif sentimen.polarity == 0.0:
        emosi = "Neutral"
    else:
        emosi = "Negatif"
    twitter.append([tweet.text, emosi])


# In[46]:


# Export to CSV
df = pd.DataFrame(twitter)

df.to_csv('DeadlineDayLive.csv', index=False, header=False)


# In[47]:


# Read CSV
read = pd.read_csv('DeadlineDayLive.csv', names=['tweet', 'sentiment'])

read

