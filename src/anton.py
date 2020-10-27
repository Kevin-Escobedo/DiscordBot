import discord
import random
import wiki
import secret #File that contains bot's token
import api_commands 
import time
from discord.ext import commands
class Anton(discord.Client):

	client = commands.Bot(command_prefix = "!")
	@client.command(name="kick", pass_context = True)
	#@commands.has_premissions(kick_members = True)
	async def kick(context, member : discord.Member, reason = ""):
		await member.kick(reason = reason)
		await context.send("User " + member.display_name + " has been kicked.")
	async def on_ready(self):
		print("ONLINE")

	async def on_message(self, message):
#Ping Pong
		if message.content.lower() == "ping":
			await message.channel.send("Pong")
#flips a coin
		if message.content.lower() == "!coin":
			await message.channel.send(self.coinFlip())
#gets wiki article		
		if message.content.split(" ",1)[0] == "!wiki":
			result = wiki.search(message.content.split(" ",1)[1].lower())
			await message.channel.send(result)
#gets a joke
		if "!joke" in message.content:
			if len(message.content.split(" ",1)) > 1:
				joke_list = api_commands.joke(message.content.split(" ",1)[1])
			else:
				joke_list = api_commands.joke()
			if len(joke_list) > 1:	
				await message.channel.send(joke_list[0])
				time.sleep(1)
				await message.channel.send("...")
				time.sleep(1)
				await message.channel.send(joke_list[1])
			else:
				await message.channel.send(joke_list[0])
#gets image
		if "!image" in message.content:
			result = api_commands.image()
			await message.channel.send(result)
#gets weather
		if "!weather" in  message.content:
			location = message.content.split(" ",1)[1]
			weather_data = api_commands.weather(location)
			await message.channel.send(weather_data)
		# if "!kick" in message.content:
		# 	member_managment.kick()
	

	def coinFlip(self) -> str:
		heads = random.randint(0, 1)

		if heads:
			return "Heads!"

		else:     return "Tails!"

if __name__ == "__main__":
    client = Anton()
    token = secret.token
    client.run(token)

 