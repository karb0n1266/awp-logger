import discord
import valve.source.a2s
import os

from discord.ext import tasks, commands

bot = commands.Bot(	command_prefix = '!' ) # Инициализация бота и префикса.

# Событие запуска бота.
@bot.event
async def on_ready():
	print("Бот {0.user} запущен!".format(bot))
	name_change.start()

@tasks.loop(seconds = 5)
async def name_change():
	SERVER_ADDRESS1 = ('46.148.138.77', 27085)
	with valve.source.a2s.ServerQuerier(SERVER_ADDRESS1) as server:
		info1 = server.info()
	await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type = discord.ActivityType.watching,	name = "на {player_count}/{max_players} игроков.".format(**info1)))

# Запуск бота.
token = os.environ.get('BOT_TOKEN')
bot.run(token)
