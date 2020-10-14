import discord
import random
import wiki
import secret #File that contains bot's token

class Anton(discord.Client):
    async def on_ready(self):
        print("ONLINE")

    async def on_message(self, message):
        '''Handles message input'''
        if message.content.lower() == "ping":
            await message.channel.send("Pong")

        if message.content.lower() == "!coin":
            await message.channel.send(self.coinFlip())

       	if message.content.split()[0] == "!wiki":
            result = wiki.search(message.content.split()[1].lower())
            await message.channel.send(result)

    def coinFlip(self) -> str:
        '''Flips a coin'''
        heads = random.randint(0, 1)

        if heads:
            return "Heads!"

        else:
            return "Tails!"

if __name__ == "__main__":
    client = Anton()
    token = secret.token
    client.run(token)