import telebot.types
from telebot import types

from core.settings import bot
from email_sender.mail import EmailSender
from google_maps_app.google_maps_route_builder import GoogleMapsRouteBuilder


@bot.message_handler(commands=['start'])
def send_greetings_msg(message: telebot.types.Message):
    # print('START', message.from_user.full_name, message.from_user.username, datetime.datetime.now())
    commands = r"""/start - Run bot and see commands
/build_way - Build a route from one place to another
/send_emails - Send some email to your recipients"""
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    full_name = first_name
    if last_name:
        full_name += f' {last_name}'
    bot.reply_to(message, f"{full_name}, you are welcome!\n{commands}")


@bot.message_handler(commands=['build_way'])
def build_way_google_maps(message: telebot.types.Message):
    # print('BUILD_WAY', message.from_user.full_name, message.from_user.username, datetime.datetime.now())
    bot.send_message(message.from_user.id, 'Please enter first place')
    bot.register_next_step_handler(message, __get_first_point)


def __get_first_point(message: telebot.types.Message):
    # if message.location is not None:
    #     lat_user = message.location.latitude
    #     lng_user = message.location.longitude
    # else:
    #     bot.send_message(message.from_user.id, 'Please send me your location')
    first_place = message.text
    bot.send_message(message.from_user.id, 'Please enter second place')
    bot.register_next_step_handler(message,
                                   __get_second_point,
                                   first_place=first_place)


def __get_second_point(message: telebot.types.Message, first_place):
    second_place = message.text
    # getting route url
    route_builder = GoogleMapsRouteBuilder(first_place, second_place)
    map_url = route_builder.get_route_url()
    # adding button
    markup = types.InlineKeyboardMarkup()
    google_map_button = types.InlineKeyboardButton("Show Route",
                                                   url=map_url)
    markup.add(google_map_button)
    bot.send_message(message.chat.id,
                     text='Route has been created!',
                     reply_markup=markup)


@bot.message_handler(commands=['send_emails'])
def send_emails_to_users(message: telebot.types.Message):
    # print('BUILD_WAY', message.from_user.full_name, message.from_user.username, datetime.datetime.now())
    bot.send_message(message.from_user.id,
                     'Please enter receivers list separated by comma')
    bot.send_message(message.from_user.id,
                     'Example: test1@gmail.com, test2@yahoo.com, test3@ukr.net')
    bot.register_next_step_handler(message, __get_receivers)


def __get_receivers(message: telebot.types.Message):
    receivers_list = message.text.split(',')
    for i in range(len(receivers_list)):
        receivers_list[i] = receivers_list[i].strip()
    bot.send_message(message.from_user.id, 'Please enter your letter subject')
    bot.register_next_step_handler(message,
                                   __get_subject,
                                   receivers_list=receivers_list)


def __get_subject(message: telebot.types.Message, receivers_list: list):
    letter_subject = message.text.strip()
    bot.send_message(message.from_user.id, 'Please enter your letter body')
    bot.register_next_step_handler(message,
                                   __get_body,
                                   receivers_list=receivers_list,
                                   letter_subject=letter_subject)


def __get_body(message: telebot.types.Message,
               receivers_list: list,
               letter_subject: str):
    letter_body = message.text
    email_sender = EmailSender(receivers=receivers_list,
                               subject=letter_subject,
                               message=letter_body)
    email_sender.send_email()
    bot.send_message(message.from_user.id, 'Successfully sent email!')


@bot.message_handler(commands=['shutdown'])
def bot_shutdown(message: telebot.types.Message):
    if message.from_user.username == 'allen_avanheim':
        print('SERVER IS TURNING OFF')
        bot.send_message(message.from_user.id, 'SERVER IS TURNING OFF')
        from os import _exit
        _exit(0)
    else:
        bot.send_message(message.from_user.id, 'You are not an admin!')
