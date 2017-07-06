# bot for reddit
# https://github.com/Maxed/reddit-bot-test

import praw
import time
import config

COMMENT_LIMIT = 200
SLEEP_TIME = 1
STRING = "hello"
SUBREDDIT = "test"

i = 0

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
def run(r):
	# check for comments in specified subreddits
	print("searching for \"" + STRING + "\" in /r/" + SUBREDDIT)
	for comment in r.subreddit(SUBREDDIT).comments(limit = COMMENT_LIMIT): # equal to the number of commments to check
		# if a certain string is in the comments then reply and log it
		if STRING in comment.body and comment.id not in open("comments.txt", "r").read() and comment.author != r.user.me():
			print("string matched in " + comment.id)
			# commented out for testing to avoid spamming
			#comment.reply("Thank You!")
			print("replied to " + comment.id)
			f = open("comments.txt", "a")
			f.write(comment.id + "\n")
			f.close()
			print("added " + comment.id + " to comments.txt")
		# sleep for 1 second to avoid spamming reddit's api
		time.sleep(SLEEP_TIME)

r = login()
run(r)
