#bot for reddit

import praw
import time

import config

def login():
	praw.Reddit(
		username = config.username,
		password = config.password,
		client_id = config.client_id,
		client_secret = config.client_secret,
		user_agent = config.user_agent)

def run():
