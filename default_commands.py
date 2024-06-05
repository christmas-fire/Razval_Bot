from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats


async def set_bot_commands(bot: Bot):
    my_commands = [
        BotCommand(command="start", description="🚀Перезапуск бота на стартовую позицию"),
        BotCommand(command="gallery", description="✏️Посмотреть примеры моих работ"),
        BotCommand(command="about", description="🎀Кое-что обо мне")
    ]
    
    await bot.set_my_commands(
        commands=my_commands, scope=BotCommandScopeAllPrivateChats()
    )