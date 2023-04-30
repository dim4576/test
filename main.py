from bot import Bot
from variables import *



bot = Bot(TOKEN_FILE_NAME)


@bot.message_handler(content_types=['text'])
def command_start(message):
    txt = f'Вот что ме удалось о тебе узнать:\n' \
          f'ты отправил: {message.text}\n' \
          f'тебя зовут: {message.from_user.first_name}\n' \
          f'твоё полное имя {message.from_user.full_name}\n' \
          f'товй юзернэйм {message.from_user.username}\n' \
          f'твой ID {message.from_user.id}\n' \
          f'с момента создания бота это {message.id} сообщение по счёту включая мои собственные\n'
    bot.send_message(message.from_user.id, txt)
    pass

bot.infinity_polling()