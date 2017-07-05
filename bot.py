# bot for reddit
# https://github.com/Maxed/reddit-bot-test

import praw
import time

import config

subreddit = "test"

comment_cache = []

# login function
def login():
	print("logging in...")

	# all login info is stored in config.py which is ignored by git
	r = praw.Reddit(
			username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = config.user_agent)

	print("logged in successfully")

	return r

# main function
def run(r, comment_cache):
	# check for comments in specified subreddits
	for comment in r.subreddit('test').comments(limit = 50):
		# if a certain string is in the comments then reply and log it
		if "hello" in comment.body and comment.id not in comment_cache and comment.author != r.user.me():
			print("string matched in " + comment.id)

			comment.reply("Thank You!")
			print("replied to " + comment.id)

			comment_cache.append(comment.id)
			if comment.id in comment_cache:
				print("added " + comment.id + " to comment cache")

	print("sleeping...")
	time.sleep(10)
	
r = login()

while True:
	run(r, comment_cache)