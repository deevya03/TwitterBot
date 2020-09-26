import tweepy
from time import sleep

print("hey i am your twitter bot")

CONSUMER_KEY = 'zeFirtcNnmtn3ttfZMVvcdLwn'
CONSUMER_SECRET = 'P7SYOpeMQH0e8zvoAkvkK2wIy1sW3loQlYj6etCN6Tf07ShpWt'
ACCESS_KEY = '864681673266520064-AYV7oQwZaQXDjYcN2NCOyN55EwrD7Ud'
ACCESS_SECRET = 'V72K5V1TKCMkulg1BS6D2lZDYqL34JxwypZ1kHp1Drsee'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

api.update_status("Retweeting by bot..")


for tweet in tweepy.Cursor(api.search, q='#100DaysofCode').items(1):
    try:
        print('\nRetweet Bot found tweet by @' + tweet.user.screen_name + '. ' + 'Attempting to retweet.')

        tweet.retweet()
        print('Retweet published successfully.')
        
        # Where sleep(10), sleep is measured in seconds.
        # Change 10 to amount of seconds you want to have in-between retweets.
        # Read Twitter's rules on automation. Don't spam!
        sleep(10)

    # Some basic error handling. Will print out why retweet failed, into your terminal.
    except tweepy.TweepError as error:
        print('\nError. Retweet not successful. Reason: ')
        print(error.reason)

    except StopIteration:
        break



for tweet in tweepy.Cursor(api.search, q=('#HelloWorld OR  #Python3 OR #100DaysofCode'),lang='en').items(2):
            try:
                # Add \n escape character to print() to organize tweets
                print('\nTweet by: @' + tweet.user.screen_name)

                # Retweet tweets as they are found
                tweet.favorite()
                print('Like the tweet')

                sleep(5)

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break