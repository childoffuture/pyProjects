import config
from moneybot import MoneyBot

# Запуск бота
bot = MoneyBot(config.TOKEN, config.money_names)
bot.start()
