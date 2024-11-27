import telebot
import random
from recepties import cocktails
bot = telebot.TeleBot("7769174544:AAH5KGSpeV4_FIgxN39JPHhy6kvGVugE_Nw")


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привіт! Надішліть команду /cocktail, щоб отримати випадковий рецепт коктейлю.")


@bot.message_handler(commands=['cocktail'])
def send_random_cocktail(message):
    cocktail_name, cocktail_recipe = random.choice(list(cocktails.items()))
    response = f"🍸 {cocktail_name}:\n{cocktail_recipe}"
    bot.send_message(message.chat.id, response)


bot.polling()




