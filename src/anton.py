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
        if message.content.lower() == "ping":
            await message.channel.send("Pong")
            
        if message.content.lower() == "!coin":
            await message.channel.send(self.coinFlip())
            
        if message.content.split(" ",1)[0] == "!wiki":
            result = wiki.search(message.content.split(" ",1)[1].lower())
            await message.channel.send(result)
            
        if "!joke" in message.content:
            joke = self.tellJoke(message.content)
            await message.channel.send(joke[0])
            if len(joke) > 1:
                time.sleep(1)
                await message.channel.send("...")
                time.sleep(1)
                await message.channel.send(joke[1])  
                
        if "!weather" in message.content:
            location = message.content.split(" ",1)[1]
            weather_data = api_commands.weather(location)
            await message.channel.send(weather_data)

        if message.content.lower() == "!stop":
            await client.logout()
            
    def coinFlip(self) -> str:
        heads = random.randint(0, 1)
        if heads:
            return "Heads!"
        else:
            return "Tails!"
        
    def tellJoke(self, theme:str) -> [str]:
        if len(theme.split(" ", 1)) > 1:
            jokeList = api_commands.joke(theme.split(" ", 1)[1])
        
        else:
            jokeList = api_commands.joke()
            
        return jokeList
    
if __name__ == "__main__":
    client = Anton()
    token = secret.token
    client.run(token)
