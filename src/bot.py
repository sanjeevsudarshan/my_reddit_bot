'''
Script plays around with reddit API
'''

import os
import re
import praw

def search_for_posts(subreddit, keyword, period):
    '''
        Module looks for keywords in posts in a subreddit within a time frame.
    '''
    sort = 'comments'
    important_results = []
    limit = 5
    searchResults = subreddit.search(keyword, sort, time_filter=period)
    for post in searchResults:
        print post.url
        important_results.append(post.url)
        limit = limit - 1
        if limit <= 0:
            return

def post_replied_to(submissionFile, submission_id):
    '''
        Module checks if the bot has already replied to a post
    '''
    if not os.path.isfile(submissionFile):
        return False
    else:
        with open(submissionFile, 'r') as subFile:
            postList = filter(None, subFile.read().split('\n'))
            if submission_id in postList:
                return True
    return False

def post_reply(subreddit, postToReplyTo, replyText):
    '''
        Module sends a reply to a post that contains certain words
    '''
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
    keyword = ""
    period = ""
    search_for_posts(subreddit, keyword, period)