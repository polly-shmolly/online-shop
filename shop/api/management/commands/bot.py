from django.conf import settings
from aiogram import Bot, Dispatcher, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils import executor
from django.core.management.base import BaseCommand
import logging
from asgiref.sync import sync_to_async
import time
from ...models import Category, Producer


logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.TELEGRAMBOT_API_TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=["help", "start"])
async def command_help(message: types.Message):
    await message.answer("input some message", reply_markup=keyboard)


button = KeyboardButton('Categories')
button_producers = KeyboardButton('Producers')
keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
keyboard.add(button)
keyboard.add(button_producers)


@sync_to_async()
def get_categories():
    return list(Category.objects.all())


@sync_to_async()
def get_producers():
    return list(Producer.objects.all())


# реакция на нажатие кнопки
@dp.message_handler(lambda message: message.text == 'Categories')
async def certain_message(msg: types.Message):
    categories = await get_categories()

    msg_to_answer = ''
    for cat in categories:
        msg_to_answer += f'Category: {cat.name}\n{cat.description}\n'
    await bot.send_message(msg.from_user.id, msg_to_answer)


# реакция на нажатие кнопки
@dp.message_handler(lambda message: message.text == 'Producers')
async def certain_message(msg: types.Message):
    producers = await get_producers()

    msg_to_answer = ''
    for p in producers:
        msg_to_answer += f'Producer: {p.name}\n'
    await bot.send_message(msg.from_user.id, msg_to_answer)


# реакция на ввод текста
@dp.message_handler()
async def query_telegram(msg: types.Message):
    print(msg.text)
    await bot.send_message(msg.chat.id, 'understandable, have a nice day')


class Command(BaseCommand):
    help = 'Test tg bot'

    def handle(self, *args, **options):
        executor.start_polling(dp)

