# piazza-slackbot
A simple bot that sends Slack notifications when new posts are added to a Piazza page.

## Why?
To get notifications without having to check the Piazza website or have email notifications clog up your inbox.

# Instructions

## Requirements
The bot is written in Python 3 and requires the following packages:
```
slacker
piazza-api
time
```

## Set-up
To set this up you need to have access to a page on Piazza and have a Slack account with the necessary permissions.

Then follow this [link](https://my.slack.com/services/new/bot) to create a bot. Once you have created a bot make sure to save the API token as you will need it to authenticate your bot.

Consider setting up a new channel for the bot so that it doesn't overrun the #general discussion. Once you have created the channel you can then add the bot by clicking `Channel Settings` > `Invite team members to join...` > and selecting your bot from the list of users.

You will need to add your credentials for both Piazza and Slack into the relevant places in the file `slackbot.py`. All the areas where you need to input information are marked with `TODO`. Simply add the relevant information to the empty strings.

An optional parameter `include_link` can be passed to the main function to include or exclude a URL to the post when the message is sent. This is set to true by default but can be changed if you do not want to include links.

## Usage
I suggest using `screen` to run the bot on a machine where it can operate constantly without any interruptions. Simply open a new screen window, run the bot by typing `python3 slackbot.py`, and then detach from the window.

The bot is set up to constantly print out statements in the window to show that it is running, although you can comment this out if you wish.
