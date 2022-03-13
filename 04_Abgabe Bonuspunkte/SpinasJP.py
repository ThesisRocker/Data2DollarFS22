import tweepy
import datetime
import xlsxwriter
import sys
import json
import pytz

ACCESS_TOKEN = "1496954246650122245-72VXeoLLc6zEtFG4nqIkFDcq3ahR8x"
ACCESS_SECRET = "yDH1ywhOa2VnXhMlJ3R4yfBqAEswlpi73RAW0oRqM9DBB"
CONSUMER_KEY = "lqi5Bq2CEht6RyNGA7YXX1nCd"
CONSUMER_SECRET = "XshZVhdMtSWtR1tVg3HL5fWrGX0ni7vCQwb7sXpTmg9mR4vFIm"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

startDate = datetime.datetime(2010, 1, 1, 0, 0, 0)
endDate = datetime.datetime(2022, 3, 7, 0, 0, 0)

utc = pytz.UTC

startDate = utc.localize(startDate)
endDate = utc.localize(endDate)

tweets = []
tweet_dict_list = []
tmpTweets = api.user_timeline(screen_name="ABack")

for tweet in tmpTweets:
    if tweet.created_at < endDate and tweet.created_at > startDate:
        tweets.append(tweet)

while (tmpTweets[-1].created_at > startDate):
    tmpTweets = api.user_timeline(screen_name="ABack", max_id=tmpTweets[-1].id)
    for tweet in tmpTweets:
        if tweet.created_at < endDate and tweet.created_at > startDate:
            tweets.append(tweet)

            tweet_dict_list.append({
                'id': tweet.id,
                'created_at': str(tweet.created_at),
                'text': tweet.text,
                'status': tweet.in_reply_to_status_id
            })

# Write JSON file
with open('SpinasJP.json', 'w') as file:
    file.write(json.dumps(tweet_dict_list))

print("Json File ready")

# Excel file
workbook = xlsxwriter.Workbook("SpinasJP.xlsx")
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
print("Fertig")
