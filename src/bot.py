'''
Script plays around with reddit API
'''

import os
import re
import praw

def post_replied_to(submissionFile, submission_id):
    if not os.path.isfile(submissionFile):
        return False
    else:
        with open(submissionFile, 'r') as subFile:
            postList = filter(None, subFile.read().split('\n'))
            if submission_id in postList:
                return True
    return False

def run_bot():

def post_reply(subreddit, postToReplyTo, replyText):
    submissionFile = 'posts_replied_to.txt'
    for submission in subreddit.hot():
        submissionId = submission.id
        if not post_replied_to(submissionFile, submissionId):
            if re.search(postToReplyTo, submission.title, re.IGNORECASE):
                submission.reply(replyText)
                with open(submissionFile, 'a') as subFile:
                    subFile.write(submissionId + '\n')
                    return

if __name__ == '__main__':
    reddit = praw.Reddit('bot1')
    subreddit = reddit.subreddit('')
    postToReplyTo = ""
    replyText = ""
    post_reply(subreddit, postToReplyTo, replyText)