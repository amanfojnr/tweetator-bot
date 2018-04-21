# !/usr/bin/env python
# -*- coding: utf-8 -*-
# This software implements a twitter application
# meant to simulate human activity on twitter
# Copyright(C) 2018
# MIT License
# Expl00ra <amanfojnr@zoho.com>

import os
import configparser
import time

import tweepy

config = configparser.ConfigParser()
config.read("config.ini")

consumer_key = config["API_KEYS"]["consumer_key"]
consumer_secret = config["API_KEYS"]["consumer_secret"]
access_token = config["API_KEYS"]["access_token"]
access_token_secret = config["API_KEYS"]["access_token_secret"]
