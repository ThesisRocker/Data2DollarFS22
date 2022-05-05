import tweepy
import datetime
import pytz
import sys
import xlsxwriter
import json 

consumerKey = "vuB4lzf15tMaZGBctnGi5Ujbo"
consumerSecret = "IczITrPYzx8AN6iX9DlX0FlVm8MmU7zx6Sswoq2gpntlIciHHo"
accessToken = "1500757114259746820-IFBF1n6j8UMOY4tUTVqj3t5vUmWdIK"
accessTokenSecret = "aEHoAPYpYjutAeX8Ve82zegHGKF1k2alYEbE98ZLBfDf6"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

startDate = datetime.datetime(2010, 1, 1, 0, 0, 0)
endDate =   datetime.datetime(2022, 3, 8, 0, 0, 0)

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

workbook = xlsxwriter.Workbook("Dreymueller_Maximilian" + ".xlsx")
worksheet = workbook.add_worksheet()
row = 0
for tweet in tweets:
    worksheet.write_string(row, 0, str(tweet.id))
    worksheet.write_string(row, 1, str(tweet.created_at))
    worksheet.write(row, 2, tweet.text)
    worksheet.write_string(row, 3, str(tweet.in_reply_to_status_id))
    row += 1

workbook.close()
print("Data saved")