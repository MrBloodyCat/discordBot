import imp
from discord.ext import commands
import discord
import json


with open('config.json', 'r') as file:
	config = json.load(file)


class User(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        activity = discord.Streaming(name = f"-help", url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")
        await self.client.change_presence(activity = activity)
        print('Бот готов')

        
def setup(client):
    client.add_cog(User(client))
