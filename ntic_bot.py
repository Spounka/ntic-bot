from discord.ext import commands
from ntic_bot import commands as com
from ntic_bot import config

bot = commands.Bot(command_prefix="$")

com.set_commands(bot=bot)

bot.run(config.bot_token)
