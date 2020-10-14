import discord
import random

class Anton(discord.Client):
    async def on_ready(self):
        print("ONLINE")

    async def on_message(self, message):
        '''Handles message input'''
        if message.content.lower() == "ping":
            await message.channel.send("Pong")

        if message.content.lower() == "!coin":
        	random_int = random.randint(1,2)
        	side = "Heads!"
        	if random_int == 2:
        		side = "Tails!"
        	await message.channel.send(side)

if __name__ == "__main__":
    client = Anton()
    token = "NzY1NjEyODAyMTg1MzYzNDc3.X4XWfA.T9AiS-MFmlNYIhn_ELHKUKj1utE"
    client.run(token)


