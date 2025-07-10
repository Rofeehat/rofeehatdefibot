from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Bot configuration (REPLACE THESE WITH YOUR ACTUAL USERNAMES)
BOT_TOKEN = "8000594605:AAEZL6drZTDInGLn2shNO5cNFlBi4BSASmA"
CHANNEL_USERNAME = "@your_channel_username"  # 👈 REPLACE WITH YOUR TELEGRAM CHANNEL
TWITTER_USERNAME = "@your_twitter_username"  # 👈 REPLACE WITH YOUR TWITTER HANDLE

async def start(update: Update, context: CallbackContext) -> None:
    """Send welcome message with join instructions"""
    keyboard = [
        [
            InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/{CHANNEL_USERNAME[1:]}"),
            InlineKeyboardButton("🐦 Follow Twitter", url=f"https://twitter.com/{TWITTER_USERNAME[1:]}")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "🎉 Welcome to the SOL Airdrop Bot!\n\n"
        "📌 To qualify for 10 SOL airdrop:\n"
        f"1. Join our Telegram channel: {CHANNEL_USERNAME}\n"
        f"2. Follow our Twitter: {TWITTER_USERNAME}\n\n"
        "👉 After completing the steps, send your Solana wallet address below!",
        reply_markup=reply_markup
    )

async def handle_wallet(update: Update, context: CallbackContext) -> None:
    """Process submitted wallet address (no real validation)"""
    wallet = update.message.text.strip()
    await update.message.reply_text(
        f"🚀 Congratulations!\n\n"
        f"10 SOL is being sent to:\n`{wallet}`\n\n"
        "⏳ Transaction should appear in your wallet within 24 hours\n"
        "🎉 Thanks for participating in our airdrop!",
        parse_mode="Markdown"
    )

def main() -> None:
    """Run the bot"""
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Command handlers
    application.add_handler(CommandHandler("start", start))
    
    # Handle all text messages as wallet submissions
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_wallet))
    
    print("✅ Bot is running... Press CTRL+C to stop")
    application.run_polling()

if __name__ == "__main__":
    main()
