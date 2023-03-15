from aiogram import Router
from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command, BaseFilter
from lexicon.lexicon import LEXICON_ADMINS
from config_data.config import set_admin_chat
from dataclasses import dataclass

#Инициализируем роутер уровня модуля
router: Router = Router()
admin = set_admin_chat()

#Cобственный фильтр для проверки админского чата
@dataclass
class IsAdmin(BaseFilter):
    admin: str

    async def __call__(self, message: Message) -> bool:
        
        return str(message.chat.id) == admin


#Хендлер для команды /admin
@router.message(Command(commands='admin'), IsAdmin(admin))
async def process_help_command(message: Message):
    await message.answer(text='сообщение для админов чата')
