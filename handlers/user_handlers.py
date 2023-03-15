from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_USERS


#Инициализируем роутер уровня модуля
router: Router = Router()


#Хендлер для команды /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_USERS['/start'])

#Хендлер для коменды /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_USERS['/help'])