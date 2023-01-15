import telebot.types
from telebot import types

from core.settings import bot
from google_maps_app.google_maps_route_builder import GoogleMapsRouteBuilder


@bot.message_handler(commands=['start'])
def send_greetings_msg(message: telebot.types.Message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    full_name = first_name
    if last_name:
        full_name += f' {last_name}'
    bot.reply_to(message, f"{full_name}, you are welcome!")


@bot.message_handler(commands=['build_way'])
def build_way_google_maps(message: telebot.types.Message):
    bot.send_message(message.from_user.id, 'Please enter first place')
    bot.register_next_step_handler(message, __get_first_point)


def __get_first_point(message: telebot.types.Message):
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
