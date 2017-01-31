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
slack_token = "" #TODO Your slack API token goes here
bot=Slacker(slack_token) #authorizing bot
channel="" #TODO Name of the channel to post to
bot_name = "" #TODO Name of your slackbot

#URL for posts on the page
POST_BASE_URL = "https://piazza.com/class/"+piazza_id+"?cid="

def check_for_new_posts(NUM_POSTS,include_link=True):
    """
    This function will run continuously,
    checking every 1 minute to see if the number of posts
    in the Piazza feed is equal to the previous number.
    If a new post is added then a message will be sent to
    Slack.
    """
    while True:
        UPDATED_NUM_POSTS = len(network.get_feed()['feed'])
        if UPDATED_NUM_POSTS > NUM_POSTS:
            attachment = None
            message = None
            if include_link is True:
                attachment = [
                    {
                        "title": "New post on Piazza!",
                        "title_link": POST_BASE_URL+str(NEW_NUM_POSTS+1),
                        "text": "Follow the link to view this post",
			            "color": "good"
                    }
                ]
            else:
                message="New post on Piazza!"
            bot.chat.post_message(channel,message, \
            as_user=bot_name,parse='full',attachments=attachment)
            NUM_POSTS = UPDATED_NUM_POSTS
        else:
            pass
        print("Slackbot is running...")
        sleep(60)

if __name__ == '__main__':
     NUM_POSTS = len(network.get_feed()['feed'])
     check_for_new_posts(NUM_POSTS)
