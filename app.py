if __name__ == '__main__':
    try:
        from core.settings import bot
    except ImportError:
        from os import system

        system('pip install --upgrade -r requirements.txt')
        from core.settings import bot
    finally:
        from handlers import *

    print('TELEGRAM BOT IS RUNNING...')
    bot.infinity_polling()
