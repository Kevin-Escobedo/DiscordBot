import discord

class Anton(discord.Client):
    async def on_ready(self):
        print("ONLINE")

    async def on_message(self, message):
        '''Handles message input'''
        if message.content.lower() == "ping":
            await message.channel.send("Pong")


if __name__ == "__main__":
    client = Anton()
    token = ""
    client.run(token)
