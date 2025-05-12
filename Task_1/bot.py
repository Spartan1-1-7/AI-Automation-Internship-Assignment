import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import youtube_search

# Load environment variables from the .env file
load_dotenv()

# Telegram Bot API Key
TELEGRAM_BOT_API_KEY = os.getenv("TELEGRAM_BOT_API_KEY")

# Start the bot
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hi! Send me a search query and I will find the best YouTube video for you.')

# Handle user messages
async def handle_message(update: Update, context: CallbackContext) -> None:
    user_query = update.message.text
    await update.message.reply_text(f"Searching for: {user_query}...")

    # Call the youtube_search.py script to get the best video
    video_url = youtube_search.search_youtube(user_query)
    
    if video_url:
        await update.message.reply_text(f"Here is the best video I found: {video_url}")
    else:
        await update.message.reply_text("Sorry, no videos found.")

def main():
    # Create the Application and pass it your bot's API token.
    application = Application.builder().token(TELEGRAM_BOT_API_KEY).build()

    # Register the /start command handler
    application.add_handler(CommandHandler("start", start))

    # Register the message handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
