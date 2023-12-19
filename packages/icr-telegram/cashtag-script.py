import telegram
import tweepy
import os

# Telegram bot token
os.environ["TELEGRAM_TOKEN"] = "1"
# Twitter API credentials
os.environ["TWITTER_CONSUMER_KEY"] = "2"
os.environ["TWITTER_CONSUMER_SECRET"] = "3"
os.environ["TWITTER_ACCESS_TOKEN"] = "4"
os.environ["TWITTER_ACCESS_TOKEN_SECRET"] = "5"

# Create the Telegram bot
bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])

# Create the Twitter API client
auth = tweepy.OAuthHandler(os.environ["TWITTER_CONSUMER_KEY"], os.environ["TWITTER_CONSUMER_SECRET"] )
auth.set_access_token(os.environ["TWITTER_ACCESS_TOKEN"], os.environ["TWITTER_ACCESS_TOKEN_SECRET"])
twitter_api = tweepy.API(auth)

# Function to handle incoming Telegram messages
def handle_message(update, context):
    chat_id = update.message.chat_id
    text = update.message.text

    # Check if the message contains a cashtag
    if text.startswith('$INJ'):
        cashtag = text[1:]
        # Search for tweets with the cashtag
        tweets = twitter_api.search(q=cashtag, tweet_mode='extended')

        # Send the tweets to the user
        for tweet in tweets:
            bot.send_message(chat_id=chat_id, text=tweet.full_text)

# Create the Telegram bot updater and dispatcher
updater = telegram.Updater(token=os.environ["TELEGRAM_TOKEN"], use_context=True)
dispatcher = updater.dispatcher

# Register the message handler function
dispatcher.add_handler(telegram.MessageHandler(telegram.Filters.text, handle_message))

# Start the bot
updater.start_polling()
