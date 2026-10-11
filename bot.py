import os
import telebot

TOKEN = os.environ["BOT_TOKEN"]
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "Welcome to Mindbot! 🤖\n"
        "Main aapka personal Telegram bot hoon.\n"
        "Madad ke liye /help likhein."
"Developer: Anant Kumar"    )

@bot.message_handler(commands=["help"])
def help_cmd(message):
    bot.reply_to(
        message,
        "Mindbot Commands:\n"
        "/start - Bot shuru karein\n"
        "/help - Madad paayein\n"
        "/about - Bot ke baare mein"
    )

@bot.message_handler(commands=["about"])
def about(message):
    bot.reply_to(message, "Mindbot 🤖\nUsername: @Anant000bot")

@bot.message_handler(func=lambda message: True)
def echo(message):
    if message.text:
        bot.reply_to(message, "Aapne kaha: " + message.text)

print("Mindbot is running...")
bot.infinity_polling()
