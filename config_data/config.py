from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
    token: str

@dataclass
class Config:
    tg_bot: TgBot



def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))

def set_admin_chat(path: str | None = None):
    env = Env()
    env.read_env(path)
    admin_chat = env('ADMIN_CHAT')
    return admin_chat
    