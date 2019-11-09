# Tweet Verified Users Script

Made with Python Version 3.7.5

This bot utilises Tweepy. It can be installed via:
```sh
    $ pip install tweepy
```

# Why?

  - Bored

# What it does?
A random number is generated and is used to try fetch the user who the ID belongs to. It then checks if the user is verified and if they are, tweets at them letting them know they're verified. The script then restarts and reruns.

If the user is not verified or the account is suspened or not existant then it will generate another number to use.

### Installation
Git Clone or just download the `verfied_tweet.py` file and just run it with `python verified_tweet.py`.

### Issues
Takes a while to actually find a verified user, which can also be a benefit to avoid spamming tweets. Can also change the sample range.

### TODO
 - Nothing it's perfect
