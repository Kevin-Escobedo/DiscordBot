import discord
import random
import wiki
import secret #File that contains bot's token
import api_commands 
import time
class Anton(discord.Client):

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
#gets weather
		if "!weather" in  message.content:
			location = message.content.split(" ",1)[1]
			weather_data = api_commands.weather(location)
			await message.channel.send(weather_data)

	def coinFlip(self) -> str:
		heads = random.randint(0, 1)

		if heads:
			return "Heads!"

		else:
			return "Tails!"

if __name__ == "__main__":
    client = Anton()
    token = secret.token
    client.run(token)

   