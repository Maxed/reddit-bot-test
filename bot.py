# bot for reddit
# https://github.com/Maxed/reddit-bot-test

import praw
import time

import config

subreddit = "test"


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
def run(r, comments_replied_to):
	# check for comments in specified subreddits
	for comment in r.subreddit('test').comments(limit = 25):
		# if a certain string is in the comments then reply and log it
		if "hello" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
			print("string matched in " + comment.id)
			comment.reply("Thank You!")

			with open()

			# comments.append(comment.id)


r = login()

run(r, comments_replied_to);