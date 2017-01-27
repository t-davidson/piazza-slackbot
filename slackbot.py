"""
This is a simple Slackbot that will
check a Piazza page for new posts every 1 minute.
Every time a new post is observed a notification will
be sent out
"""

from piazza_api import Piazza
from slacker import Slacker
from time import sleep

#Accessing Piazza and loading data
piazza_id = "" #TODO this is the suffix of the piazza url
piazza_email = "" #TODO your email
piazza_password = "" #TODO your piazza piazza_password
p = Piazza()
p.user_login(email=piazza_email, password=piazza_password)
network = p.network(piazza_id)

#Accessing Slack and configuring the bot
slack_token = "" #TODO Your slack bot token goes here
bot=Slacker(slack_token) #authorizing bot
channel='' #TODO Name of the channel to post to
bot_name = '' #TODO Name of your slackbot
message="New message on Piazza!"#TODO Message to send

def check_for_new_posts(NUM_POSTS):
    """
    This function will run continuously,
    checking every 1 minute to see if the number of posts
    in the Piazza feed is equal to the previous number.
    If a new post is added then a message will be sent to
    Slack.
    """
    while True:
        feed = network.search_feed('')
        if len(feed) > NUM_POSTS:
            bot.chat.post_message(channel,message, \
            as_user=bot_name,parse='full')
            NUM_POSTS = len(feed)
        else:
            pass
        print("Slackbot is running...")
        sleep(60)

if __name__ == '__main__':
     NUM_POSTS = len(network.search_feed(''))
     check_for_new_posts(NUM_POSTS)
