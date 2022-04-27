import discord
from discord.ext import commands
import time


class User(commands.Cog):
    def __init__(self, client):
        self.client = client

# -------------------------------------------------------------------------------------------
    # новости

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def new(self, ctx, img=None, *, msg=None):
        if ctx.author.id == 227117061011144704:
            await ctx.message.delete()
            if img is None:
                embed = discord.Embed(
                    description="💢Неправильный ввод команды", color=0xff4700)
                msgg = await ctx.send(embed=embed)
                time.sleep(5)
                await msgg.delete()
                return
            if msg is None:
                embed = discord.Embed(
                    description="💢Неправильный ввод команды", color=0xff4700)
                msgg = await ctx.send(embed=embed)
                time.sleep(5)
                await msgg.delete()
                return

            if "https:" in img:
                embed = discord.Embed(description=f"{msg}", timestamp=ctx.message.created_at, color=0x2f3136)
                embed.set_image(url=f'{img}')

            else:
                embed = discord.Embed(description=f"{img} {msg}", timestamp=ctx.message.created_at, color=0x2f3136)

            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(User(client))
