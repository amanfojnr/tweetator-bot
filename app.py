# !/usr/bin/env python
# -*- coding: utf-8 -*-
# This software implements a twitter application
# meant to simulate human activity on twitter
# Copyright(C) 2018
# MIT License
# Expl00ra <amanfojnr@zoho.com>

import os
import time
from random import randrange

import tweepy

consumer_key = os.environ["CONSUMER_KEY"]
consumer_secret = os.environ["CONSUMER_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

# setup app
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def main():
    """
    Retweets and favorites 2 picked tweets randomly from
    timeline
    """
    while True:
        home_tweets = api.home_timeline()[:10]  # pick top 10 tweets in newsfeed
        status1 = api.retweet(home_tweets[randrange(0, 10)].id)  # retweet one at random
        print(status1.text + " -- rt")
        time.sleep(10)  # wait for 10s
        status2 = api.create_favorite(home_tweets[randrange(0, 10)].id)  # favorite one at random
        print(status2.text + " -- <3")
        time.sleep(900)  # wait for 15mins

if __name__ == "__main__":
    print("afiax --> tweetator has started")
    main()