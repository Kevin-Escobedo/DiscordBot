import discord
import random
import wiki
import secret #File that contains bot's token
import api_commands 
import time
from discord.ext import commands

#create client
client  = commands.Bot(command_prefix = "!")

##################################################

@client.event
async def on_ready():
	print("ONLINE")

##################################################

#ping pong
@client.command()
async def ping(ctx):
	await ctx.send("Pong")

#flips a coin
@client.command()
async def coin(ctx):
	heads = random.randint(0, 1)
	if heads:
		await ctx.send("Heads!")
	else:
		await ctx.send("Tails!") 

##################################################

#gets wiki article		
@client.command(name = "wiki")
async def _wiki(ctx, arg):
	result = wiki.search(arg)
	await ctx.send(result)

		
#gets a joke
@client.command()
async def joke(ctx, arg=""):
	if arg != "":
		joke_list = api_commands.joke(arg)
	else:
		joke_list = api_commands.joke()

##################################################

@client.command()
async def kick(ctx, member: discord.Member, *, reason = "reason unknown"):
    await member.kick()
    await ctx.send("User @"+ member.display_name + " was kicked for " + reason)

#####BAN/UNBAN#####
@client.command()
async def ban(ctx, member: discord.Member, reason = "reason unknown"):
    await member.ban()
    await ctx.send("User @"+ member.display_name + " was banned for "+ reason)

##################################################

#run bot
client.run(secret.token)

 