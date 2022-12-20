import random

from aiogram import Bot, types, utils
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN = 'token'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def hello_message(message):
    await bot.send_message(message.chat.id, "Жоский бот слушает")
    await bot.send_message(message.chat.id,
                           "Вот мои функции брат:"
                           "\n/menu - основные функции бота\n"
                           "/how_joski_am_i - насколько ты жоский\n "
                           "/coffee - какой жоский кофе попить\n"
                           "/movie_rec - какой жоский фильмец посмотреть\n"
                           "/palindrome <строка> - жоская проверка на палиндром\n"
                           "/factorial <число> - жоский рассчёт факториала")


@dp.message_handler(commands=['menu'])
async def hello_message(message):
    await bot.send_message(message.chat.id,
                           "Вот мои функции брат:"
                           "\n/menu - основные функции бота\n"
                           "/how_joski_am_i - насколько ты жоский\n"
                           "/coffee - какой жоский кофе попить\n"
                           "/movie_rec - какой жоский фильмец посмотреть\n"
                           "/palindrome <строка> - жоская проверка на палиндром\n"
                           "/factorial <число> - жоский рассчёт факториала")


sticker25 = ["CAACAgIAAxkBAAEG3UtjndwH1RYiX3STkvSGRbrsoF1hmQACbhEAAnb8yUuO9uSCslmfOSwE",
             "CAACAgIAAxkBAAEG3VNjndxFUhk-1mYkX_t6kzixe2DKOAACSBgAAguqyEt9mn6NENQmYiwE",
             "CAACAgIAAxkBAAEG3WBjnd0YhhtySWTS9MNidN-TPNupfwACSwADa-NyEKZOJScHWrvOLAQ",
             "CAACAgIAAxkBAAEG3Wxjnd2QBKb8HCllyGmBdSDLZXiaOAACaAADGf9bI8E1qwTOqjPxLAQ",
             "CAACAgIAAxkBAAEG3W5jnd29g5EWzLtici84liphZO393QACNBsAAnaxGErTP_m3dtvenSwE"]
sticker50 = ["CAACAgIAAxkBAAEG3XBjnd3AHOBgoDoG0HhiAmDwZCnbPAACZR8AAkgywEkv18Slu1HehSwE",
             "CAACAgIAAxkBAAEG3Whjnd1ivoLDhWNwnE6CXVW9tkF5WgAClRIAAhJg6UtOycjPNTXgwCwE",
             "CAACAgIAAxkBAAEG3Xljnd-7XrmgVzrTcdm3Z311EL2b1AACEhMAAjZJyUnEeTlEmeP9vywE",
             "CAACAgIAAxkBAAEG3X1jnd_IPzAW9ElTehGQeLzP7B-0RAACpx0AA-toSnLkYT2ZAZzDLAQ",
             "CAACAgIAAxkBAAEG3X9jnd_kKjRFWPnd3xqB1khYMujVmAACXxYAAgq6yUsjtyMt_mlHPiwE"]
sticker75 = ["CAACAgIAAxkBAAEG3Wpjnd18QWuOxVh34Gf478qbra8CRwAChiEAApvVqEgiZATWRil-0ywE",
             "CAACAgIAAxkBAAEG3WRjnd1Y58XjrfsnlAiB2ZViG8nk4QACMBIAAueE6EsU2zrjGQpqCCwE",
             "CAACAgIAAxkBAAEG3VFjndwzjf62Ud5suYELvdbFvkrdSwACwR4AAoJCkEq7SCx2G7aiTiwE",
             "CAACAgIAAxkBAAEG3U1jndwTH1juhOySaQlRHPaKWv9cywAC0BIAAoq_yEva4d4GHNlQiSwE",
             "CAACAgIAAxkBAAEG3YNjneBdhb4nHievscmMzmfIb20DRgACkxoAAgcYeUvTCuqb3AUgsSwE"]
sticker100 = ["CAACAgIAAxkBAAEG3XJjnd3D4HybqHTx9d72oMq4IeUgFQAC7SMAAuQi2UmimCnozl-11iwE",
              "CAACAgIAAxkBAAEG3WZjnd1avC1O4kwwwV3sDNHsUeKUbgACmhQAAno06Et56M0wMhiQfSwE",
              "CAACAgIAAxkBAAEG3WJjnd1R_CFV5eyY5FwyYSZzM-ZyPAAC5BQAAqt86UviEhEqhf3MYiwE",
              "CAACAgIAAxkBAAEG3U9jndwYVpcKnRTolYKBdj3oJZxq_QACjBMAAm14yUs0SD5PPsFchywE",
              "CAACAgIAAxkBAAEG3Uljndv5skoVyvPttHSC7Cbi77kTfQACuxkAAtE-yUuUxGQ9tPmxpywE"]


def Joski():
    percent = random.randint(0, 100)
    ls = [percent]
    if percent < 25:
        ls.append(sticker25[random.randint(0, 4)])
    elif percent < 50:
        ls.append(sticker50[random.randint(0, 4)])
    elif percent < 75:
        ls.append(sticker75[random.randint(0, 4)])
    elif percent < 100:
        ls.append(sticker100[random.randint(0, 4)])
    return ls


@dp.message_handler(commands=['how_joski_am_i'])
async def hello_message(message):
    ls = Joski()
    await bot.send_message(message.chat.id, "Ты на " + str(ls[0]) + "% жоский")
    await bot.send_sticker(message.chat.id, ls[1])


ls_coffee = [["Латте", "https://coffee61.ru/wa-data/public/photos/68/03/368/368.970.jpg"],
             ["Kaпучино", "https://yagoda.coffee/shop/admin/uploads/fbc47823c39d2e94c7489d7a4c993a32f4848b94016.jpg"],
             ["Флэт Уайт", "https://shop.tastycoffee.ru/files/shares/data/blog/capuccino-latte-flatwhite/image100.jpg"],
             ["Эспрессо", "https://static.insales-cdn.com/images/articles/1/5497/1742201/Espresso.png"],
             ["Эспрессо Тоник", "https://shop.tastycoffee.ru/files/shares/data/blog/espresso-tonic/image2.jpg"],
             ["Американо", "https://coffeefan.info/wp-content/uploads/2018/08/kofe-amerikano-v-domashnix-usoviyax.jpg"]]


@dp.message_handler(commands=['coffee'])
async def hello_message(message):
    pair = random.choice(ls_coffee)
    await bot.send_message(message.chat.id, "Выпей жоского " + pair[0] + " бро")


@dp.message_handler(commands=['coffee'])
async def hello_message(message):
    pair = random.choice(ls_coffee)
    await bot.send_message(message.chat.id, "Выпей жоского " + pair[0] + " бро")


movies = ["Побег из Шоушенка\nЖанр: драма", "Тёмный рыцарь\nЖанр: боевик, детектив, драма",
          "Список Шиндлера\nЖанр: драма, биография, исторический фильм",
          "Криминальное чтиво\nЖанр: чёрная комедия, драма",
          "Начало\nЖанр: боевик, мистический фильм, научная фантастика",
          "Матрица\nЖанр: научная фантастика, боевик, приключение",
          "Молчание ягнят\nЖанр: детектив, мистический фильм", "Зелёная миля\nЖанр: детектив, драма, фэнтези",
          "Назад в будущее\nЖанр: научная фантастика, приключение, семейный фильм",
          "Гладиатор\nЖанр: боевик, приключение, драма"]


@dp.message_handler(commands=['movie_rec'])
async def hello_message(message):
    await bot.send_message(message.chat.id, random.choice(movies))


def fact(num):
    if num == 1:
        return 1
    return num * fact(num - 1)


@dp.message_handler(commands=['factorial'])
async def hello_message(message):
    num = message.get_args()
    if num == "":
        await bot.send_message(message.chat.id, "Брат джан, ты забыл число")
    else:
        args = num.split()
        if len(args) > 1:
            await bot.send_message(message.chat.id, "Брат джан, слишком много аргументов")
        else:
            if int(num) > 985:
                await bot.send_message(message.chat.id, "Слишком большое число:)")
            else:
                await bot.send_message(message.chat.id, "Жоский " + str(num) + "! = " + str(fact(int(args[0]))))


def is_palindrome(s):
    return s == s[::-1]


@dp.message_handler(commands=['palindrome'])
async def hello_message(message):
    string = message.get_args()
    if string == "":
        await bot.send_message(message.chat.id, "Брат джан, ты забыл ввести строку")
    else:
        if is_palindrome(string) is True:
            await bot.send_message(message.chat.id, "Твоя строка жоский палиндром")
        else:
            await bot.send_message(message.chat.id, "Твоя строка жоский НЕ палиндром")


executor.start_polling(dp)
