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


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        """ retweets or favorites incoming status """

        task_id = randrange(0, 2)
        self.retweet(status) if task_id else self.favorite(status)

    def retweet(self, status):
            api.retweet(status.id)
            print("RT -- " + status.text)
            time.sleep(60 * 15)

    def favorite(self, status):
            api.create_favorite(status.id)
            print("<3 -- " + status.text)
            time.sleep(60 * 15)

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False


def main():
    myStream = MyStreamListener()
    myStream = tweepy(auth=api.auth, listener=MyStreamListener)

    myStream.filter(track=[
        'python', 'blockchain', 'machinelearning',
        'code', 'programming', 'data',
        'ai', 'ethereum', 'c++', 'crypto',
        'golang',
    ])


if __name__ == "__main__":
    print("afiax --> tweetator has started")
    main()
