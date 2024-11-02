import telebot
from sicret import token

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши интересующий продукт для разложения!")

@bot.message_handler(commands=['листья'])
def send_hello(message):
    bot.reply_to(message, "разлагаются 1-3 месяца пищевые отходы")

@bot.message_handler(commands=['кожура_от_банана'])
def send_hello(message):
    bot.reply_to(message, "разлагаются 1-3 месяца пищевые отходы")

@bot.message_handler(commands=['ветки'])
def send_hello(message):
    bot.reply_to(message, "разлагаются 1-3 месяца пищевые отходы")


@bot.message_handler(commands=['пищевые_отходы'])
def send_bye(message):
    bot.reply_to(message, "2-4 недели")
    
@bot.message_handler(commands=['помет'])
def send_hello(message):
    bot.reply_to(message, "10-30 дней")

@bot.message_handler(commands=['апельсиновая_кожура'])
def send_bye(message):
    bot.reply_to(message, "6 месяцев")

@bot.message_handler(commands=['древесные_остатки'])
def send_hello(message):
    bot.reply_to(message, "до 10 лет")

@bot.message_handler(commands=['одежда_из_тканей'])
def send_bye(message):
    bot.reply_to(message, "разлагается за 2-3 года")

@bot.message_handler(commands=['шерстяные_изделия'])
def send_hello(message):
    bot.reply_to(message, "1 год")

@bot.message_handler(commands=['обувь'])
def send_hello(message):
    bot.reply_to(message, "4 года")

@bot.message_handler(commands=['газеты'])
def send_hello(message):
    bot.reply_to(message, "2 года")

@bot.message_handler(commands=['книги'])
def send_hello(message):
    bot.reply_to(message, "2 года")

@bot.message_handler(commands=['железная_банка'])
def send_hello(message):
    bot.reply_to(message, "10 лет")

@bot.message_handler(commands=['синтетическая_одежда'])
def send_hello(message):
    bot.reply_to(message, "30-40 лет")

@bot.message_handler(commands=['жестяная_банка'])
def send_hello(message):
    bot.reply_to(message, "до 90 лет")

@bot.message_handler(commands=['окурок'])
def send_hello(message):
    bot.reply_to(message, "до 3 лет")

@bot.message_handler(commands=['металлические_контейнеры'])
def send_hello(message):
    bot.reply_to(message, "разрушаются в морской среде за 10 лет, а бетонированные - 30 лет")

@bot.message_handler(commands=['обувь_из_искусственной_кожи'])
def send_hello(message):
    bot.reply_to(message, "40-50 лет")

@bot.message_handler(commands=['жевательная_резинка'])
def send_hello(message):
    bot.reply_to(message, "в теплых климатических условиях - 30 лет, на холоде - сотни лет")

@bot.message_handler(commands=['губка_для_мытья_посуды'])
def send_hello(message):
    bot.reply_to(message, "200 лет")

@bot.message_handler(commands=['подгузник'])
def send_hello(message):
    bot.reply_to(message, "около 500 лет")

@bot.message_handler(commands=['фольга'])
def send_hello(message):
    bot.reply_to(message, "100 лет")

@bot.message_handler(commands=['резина'])
def send_hello(message):
    bot.reply_to(message, "100 лет")

@bot.message_handler(commands=['пластик'])
def send_hello(message):
    bot.reply_to(message, "100 лет")

@bot.message_handler(commands=['аккумуляторы'])
def send_hello(message):
    bot.reply_to(message, "100 лет")

@bot.message_handler(commands=['батарейки'])
def send_hello(message):
    bot.reply_to(message, "100 лет")

@bot.message_handler(commands=['кирпич'])
def send_hello(message):
    bot.reply_to(message, "100 лет")

@bot.message_handler(commands=['бетон'])
def send_hello(message):
    bot.reply_to(message, "100 лет")

@bot.message_handler(commands=['автомобильные_покрышки'])
def send_hello(message):
    bot.reply_to(message, "120-140 лет")

@bot.message_handler(commands=['полиэтилен'])
def send_hello(message):
    bot.reply_to(message, "100-200 лет")

@bot.message_handler(commands=['стекло'])
def send_hello(message):
    bot.reply_to(message, "более 1000 лет")

@bot.message_handler(commands=['алюминиевая_тара'])
def send_hello(message):
    bot.reply_to(message, "500 лет")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
bot.polling(none_stop=True)