import tweepy
import datetime
import xlsxwriter
import sys
import pytz

ACCESS_TOKEN = "1497952793310728207-mEfsRD5Jg6oQi53U8T8R1vcdDgb9Wk"
ACCESS_SECRET = "sMmntuf9zThbe06hOqRRH3GQ5nHQ3BB4s5iuW7OiPcqrJ"
CONSUMER_KEY = "Y6nttdkvgaQUkceVPVnuTenom"
CONSUMER_SECRET = "kDpVDWasWbuFFNZ8qU34yFXxxuvwiMeTM0Zb3g0Pgn87Kjp4Z1"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

startDate = datetime.datetime(2010, 1, 1, 0, 0, 0)
endDate =   datetime.datetime(2022, 3, 7, 0, 0, 0)

utc=pytz.UTC

startDate = utc.localize(startDate) 
endDate = utc.localize(endDate) 

tweets = []
tmpTweets = api.user_timeline(screen_name="ABack")
for tweet in tmpTweets:
    if tweet.created_at < endDate and tweet.created_at > startDate:
        tweets.append(tweet)

while (tmpTweets[-1].created_at > startDate):
    tmpTweets = api.user_timeline(screen_name="ABack", max_id = tmpTweets[-1].id)
    for tweet in tmpTweets:
        if tweet.created_at < endDate and tweet.created_at > startDate:
            tweets.append(tweet)

workbook = xlsxwriter.Workbook("deCelleSinaid" + ".xlsx")
worksheet = workbook.add_worksheet()
row = 0
for tweet in tweets:
    worksheet.write_string(row, 0, str(tweet.id))
    worksheet.write_string(row, 1, str(tweet.created_at))
    worksheet.write(row, 2, tweet.text)
    worksheet.write_string(row, 3, str(tweet.in_reply_to_status_id))
    row += 1

workbook.close()
print("Excel file ready")
