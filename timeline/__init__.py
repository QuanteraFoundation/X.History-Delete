import time

from browser.Chrome import openPage
from profile.account.my import user
from startup import scrollDown

home = f"https://twitter.com/{user}"
replies = f"{home}/with_replies"
media = f"{home}/media"
likes = f"{home}/likes"
section = replies

def toTimeline():
    openPage(section)
    time.sleep(3)
    scrollDown()
    time.sleep(1)
    print("Opened Home")
