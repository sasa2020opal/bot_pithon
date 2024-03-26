import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
from aiogram.utils import executor

# Задайте ваш токен бота
API_TOKEN = '6809237237:AAFPYLUIDTk6yKFQkiJq4oxIHUaGrQCo6do'

# Задайте словник з назвами фільмів та посиланнями на них
movies = {
    "Film 1": "https://example.com/film1",
    "Film 2": "https://example.com/film2",
    "Film 3": "https://example.com/film3"
}

# Ініціалізуємо логування
logging.basicConfig(level=logging.INFO)

# Створюємо об'єкт бота та диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Обробник команди /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Welcome to the Movie Bot! Use /movies to see available movies.")

# Обробник команди /movies
@dp.message_handler(commands=['movies'])
async def show_movies(message: types.Message):
    movie_list = "\n".join([f"{movie}: {link}" for movie, link in movies.items()])
    await message.reply(f"Available Movies:\n\n{movie_list}", parse_mode=ParseMode.HTML)

# Запускаємо бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)