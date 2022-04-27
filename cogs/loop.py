from discord.ext import commands, tasks
import aiohttp
import json
from boticordpy import BoticordClient

with open('config.json', 'r') as file:
	config = json.load(file)

sdc_token = config['settings']['bots.server-discord']

class User(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.boticord = BoticordClient(self.client, config['settings']['boticord'])
        self.monitorings.start()

    @tasks.loop(hours = 1)
    async def monitorings(self):
        bot_id = self.client.user.id
        servers = len(self.client.guilds)
        users = len(self.client.users)
        stats = {"servers": servers, "shards": 1, "users": users}
        
        await self.boticord.Bots.postStats(stats)
        async with aiohttp.ClientSession() as session:
            await session.post(f"https://api.server-discord.com/v2/bots/{bot_id}/stats", headers = {"Authorization": f"SDC {sdc_token}"}, data = {"shards": 1, "servers": servers})
            await session.close()


    @monitorings.before_loop
    async def before_printer(self):
        await self.client.wait_until_ready()

def setup(client):
    client.add_cog(User(client))