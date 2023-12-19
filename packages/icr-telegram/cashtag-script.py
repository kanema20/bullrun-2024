import telegram
import tweepy

# Telegram bot token
telegram_token = 'YOUR_TELEGRAM_TOKEN'

# Twitter API credentials
consumer_key = 'YOUR_TWITTER_CONSUMER_KEY'
consumer_secret = 'YOUR_TWITTER_CONSUMER_SECRET'
access_token = 'YOUR_TWITTER_ACCESS_TOKEN'
access_token_secret = 'YOUR_TWITTER_ACCESS_TOKEN_SECRET'

# Create the Telegram bot
bot = telegram.Bot(token=telegram_token)

# Create the Twitter API client
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
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
updater = telegram.Updater(token=telegram_token, use_context=True)
dispatcher = updater.dispatcher

# Register the message handler function
dispatcher.add_handler(telegram.MessageHandler(telegram.Filters.text, handle_message))

# Start the bot
updater.start_polling()
