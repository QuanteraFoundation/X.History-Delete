from .untweet import deleteTweets, findTweet
from .unretweet import deleteRetweets
from timeline import toTimeline

def hasTweet():
    return len(findTweet())


def deleteAll():
    toTimeline()
    has_tweet = hasTweet()
    while has_tweet:
        rc = deleteTweets()
        rc1 = deleteRetweets()
        if rc == -1 or rc1 == -1:
            '''Reload if any Click() errors'''
            print("Recovering from Error!")
            toTimeline()
        has_tweet = hasTweet()
