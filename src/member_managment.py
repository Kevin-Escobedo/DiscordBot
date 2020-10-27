import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!")
@bot.command()	
async def kick(context, user : discord.Member, reason = ""):
	await Member.kick(reason = reason)