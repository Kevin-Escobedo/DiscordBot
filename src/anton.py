import discord
import random
import wikipedia
class Anton(discord.Client):
    async def on_ready(self):
        print("ONLINE")

    async def on_message(self, message):
        '''Handles message input'''
        if message.content.lower() == "ping":
            await message.channel.send("Pong")
#coinflip
        if message.content.lower() == "!coin":
        	random_int = random.randint(1,2)
        	side = "Heads!"
        	if random_int == 2:
        		side = "Tails!"
        	await message.channel.send(side)
       	if "!wiki " in message.content.lower():
       		articles = wikipedia.search(message.content.lower(), results=2)
       		print(articles)
       		if len(articles) != 0:
       			try:
       				summary = wikipedia.summary(articles[1],sentences=2)
       			except:
       				await message.channel.send('Sorry, there was an error getting info about "' + articles[1]+'"')
       			await message.channel.send(summary)
       		else:
       			await message.channel.send("Sorry, it seems like I can't find anything about your desired subject.")
if __name__ == "__main__":
    client = Anton()
    token = "NzY1NjEyODAyMTg1MzYzNDc3.X4XWfA.-4zZcb5UjGuPhFhY1yoYFleXvHI"
    client.run(token)


