import praw


reddit = praw.Reddit(client_id='va-Q0pGT0Xm0Kw',
                     client_secret='28IB7cCO3HruZJjjcq3Qh7Dw6rA',
                     username = 'seanconneryifierbot',
                     password = 'seanconneryifierbot',
                     )
                     
subreddit = reddit.subreddit('copypasta')
for submission in subreddit.stream.submissions():
    
                     
                     
