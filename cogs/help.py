import discord
from discord.ext import commands
# import aiohttp
#import psutil

class User(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def help(self, ctx):
        ms = str(self.client.latency)[:5]
        gs = len(self.client.guilds)
        # cpu = psutil.cpu_percent(4)
        # memory = str(psutil.virtual_memory()[3])[:-6]      \n` Процессор  ` ➔ `{cpu} %`\n` Оперативка ` ➔ `{memory} МБ`

        embed = discord.Embed(title = '📜 Информация',description = f'**Статистика:**\n` Отладка    ` ➔ `{ms} мс`\n` Серверов   ` ➔ `{gs}`\n\n**Ссылки:**\n` Наш Сервер    ` ➔ [` Открыть `](https://discord.gg/TwJBK3KYgs)\n` Наш API       ` ➔ [` Открыть `](https://disapi.ru)\n` Мониторинг #1 ` ➔ [` Открыть `](https://bots.server-discord.com/694590734812053537)\n` Мониторинг #2 ` ➔ [` Открыть `](https://boticord.top/bot/694590734812053537)\n\n**Основные команды:**\n` -gif          ` ➔ ` гифки действий   `\n` -nsfw         ` ➔ ` nsfw контент     `\n` -anime        ` ➔ ` Случайное аниме  `\n` -hentai       ` ➔ ` Случайный хентай `\n` -findanime    ` ➔ ` Найти аниме      `\n` -findhentai   ` ➔ ` Найти хентай     `\n` -meme         ` ➔ ` Случайный мем    `', color=0xe6fff8)
        embed.set_thumbnail(url = self.client.user.avatar_url)
        embed.set_footer(text=f'Разработчик: Bloodycat#8552')
        await ctx.send(embed=embed)

    # @commands.command()
    # @commands.has_permissions(administrator=True)
    # async def apis(self, ctx):
    #     if ctx.author.id == 227117061011144704:
    #         async with aiohttp.ClientSession() as ses:
    #             data = await ses.get('https://disapi.ru/statistics')
    #             if data.status != 200:
    #                 return
    #             data = await data.json()
    #             req = data['requests_per_hour']
    #             embed = discord.Embed(description = f'` Запросов за час: ` ➔ `{req}', timestamp=ctx.message.created_at, color=0xe6fff8)
    #             await ctx.send(embed=embed)


def setup(client):
    client.add_cog(User(client))