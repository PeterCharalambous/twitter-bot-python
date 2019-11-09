import tweepy
import random
import sys
import os

sys.tracebacklimit = 0

#Twitter keys
consumer_key=''
consumer_secret=''
access_token=''
access_token_secret=''

#Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Try finding first valid user
while True:
    #Get a random ID between 500000 and 9999999999
    target_id = random.sample(range(500000, 9999999999), 1)
    try:
        print ('Fetching user ID: ' + str(target_id[0]))
        user = api.get_user(target_id)
        print ('User verification status: ' + str(user.verified))
        if user.verified == True:
            print ('Found verified user: ' + user.name)
            break
    except tweepy.error.TweepError:
        #Suspended accounts trigger as errors. Ignore all erros
        print ('Invalid User')
        pass

print('Creating message')
message = 'I am the verified bot. @' + user.screen_name + ', just letting you know you\'re verified.'

print('Sending tweet')
api.update_status(message)

print('Restarting')

#After completion, restart script
python = ''
#Format path to cater for spaces
python = "\"{}\"".format(python)
os.execl(python, python, "\"{}\"".format(sys.argv[0]))