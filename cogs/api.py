import discord
from discord.ext import commands
import aiohttp

class User(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def meme(self, ctx):
        async with aiohttp.ClientSession() as ses:
            data = await ses.get('https://disapi.ru/meme/random')
            if data.status != 200:
                return
            data = await data.json()
            url = data['url']

            embed = discord.Embed(description = '', color=0xe6fff8)
            embed.set_image(url=url)
            await ctx.send(embed=embed)

    @commands.command()
    async def gif(self, ctx, gif = None):
        async with aiohttp.ClientSession() as ses:
            if gif is None:
                data = await ses.get('https://disapi.ru/gif/list')
                data = await data.json()
                list = '**Список категорий:**\n'
                for x in data['list']:
                    list += f' `{x}`,' 
                
                list = f'{list[:-1]}\n**Пример команды:**\n` -gif kiss `'
                embed = discord.Embed(description = list, color=0xe6fff8)
                await ctx.send(embed=embed)
                return

            if gif == 'list':
                return

            data = await ses.get(f'https://disapi.ru/gif/{gif}')
            if data.status != 200:
                return
            data = await data.json()

            url = data['url']
            height = data['height']
            width = data['width']

            embed = discord.Embed(description = '', color=0xe6fff8)
            embed.set_image(url=url)
            embed.set_footer(text=f'height: {height} | width: {width}')
            await ctx.send(embed=embed)

    @commands.command()
    async def nsfw(self, ctx, nsfw = None):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as ses:
                if nsfw is None:
                    data = await ses.get('https://disapi.ru/nsfw/list')
                    data = await data.json()
                    list = '**Список категорий:**\n'
                    for x in data['list']:
                        list += f' `{x}`,' 
                    
                    list = f'{list[:-1]}\n**Пример команды:**\n` -nsfw neko `'
                    embed = discord.Embed(description = list, color=0xe6fff8)
                    await ctx.send(embed=embed)
                    return

                if nsfw == 'list':
                    return

                data = await ses.get(f'https://disapi.ru/nsfw/{nsfw}')
                if data.status != 200:
                    return
                data = await data.json()

                url = data['url']
                height = data['height']
                width = data['width']

                embed = discord.Embed(description = '', color=0xe6fff8)
                embed.set_image(url=url)
                embed.set_footer(text=f'height: {height} | width: {width}')
                await ctx.send(embed=embed)
            
        else:
            embed = discord.Embed(description = '💢Канал не является NSFW-каналом', color=0xe6fff8)
            await ctx.send(embed=embed)

    @commands.command()
    async def hentai(self, ctx, info = None, id = None):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as ses:
                if info is None:
                    embed = discord.Embed(description = '**Пример команд:**\n` -hentai random `\n` -hentai (категория) (текст) `\n**Посмотреть списки под категории:**\n` -hentai censored `\n` -hentai year `\n` -hentai genres `', color=0xe6fff8)
                    await ctx.send(embed=embed)
                    return

                list_all = ['censored', 'year', 'genres', 'random']
                if info not in list_all:
                    return

                if id is None:
                    if info != 'random':
                        data = await ses.get(f'https://disapi.ru/hentai/{info}/list')
                        data = await data.json()
                        list = '**Список:**\n'
                        for x in data['list']:
                            list += f' `{x}`,' 
                        
                        list = f'{list[:-1]}\n**Пример команды:**\n` -hentai {info} {data["list"][0]} `'
                        embed = discord.Embed(description = list, color=0xe6fff8)
                        await ctx.send(embed=embed)
                        return

                if info == 'random':
                    data = await ses.get('https://disapi.ru/hentai/random')
                    data = await data.json()
                
                else:
                    data = await ses.get(f'https://disapi.ru/hentai/{info}/{id}')
                    if data.status != 200:
                        return
                    data = await data.json()

                if data['genres']:
                    genres = ''
                    for x in data['genres']:
                        genres += f'{x}, '
                    genres = genres[:-2]

                episodes = data['episodes']
                name = data['name']
                poster = data['poster']
                year = data['year']
                studio = data['studio']
                censored = data['censored']

                text = ''
                if censored == True:
                    text += f'Цензура: `Присутствует`\n'

                if censored == False:
                    text += f'Цензура: `Отсутствует`\n'

                if episodes:
                    text += f'Эпизоды: `{episodes}`\n'

                if year:
                    text += f'Год выхода: `{year}`\n'

                if studio:
                    text += f'Студия: `{studio}`\n'

                if data['genres']:
                    text += f'Жанры: `{genres}`\n'
        
                text = text[:-1]

                embed = discord.Embed(title = name, description = text, color=0xe6fff8)
                embed.set_image(url=poster)
                await ctx.send(embed=embed)

        else:
            embed = discord.Embed(description = '💢Канал не является NSFW-каналом', color=0xe6fff8)
            await ctx.send(embed=embed)

    @commands.command()
    async def anime(self, ctx, info = None, id = None):
        async with aiohttp.ClientSession() as ses:
            if info is None:
                list = ['type', 'year', 'rating', 'genres']
                embed = discord.Embed(description = '**Пример команд:**\n` -anime random `\n` -anime (категория) (текст) `\n**Посмотреть списки под категории:**\n` -anime type `\n` -anime year `\n` -anime rating `\n` -anime genres `', color=0xe6fff8)
                await ctx.send(embed=embed)
                return

            if info == 'random':
                pass
            
            elif info == 'type':
                inf = 'type_ru'

            elif info == 'genres':
                inf = 'genres_ru'

            elif info == 'year':
                inf = 'year'
                pass

            elif info == 'rating':
                inf = 'rating'
                pass

            else:
                return

            if id is None:
                if info != 'random':
                    data = await ses.get(f'https://disapi.ru/anime/{inf}/list')
                    data = await data.json()
                    list = '**Список:**\n'
                    for x in data['list']:
                        list += f' `{x}`,' 
                    
                    list = f'{list[:-1]}\n**Пример команды:**\n` -anime {info} {data["list"][0]} `'
                    embed = discord.Embed(description = list, color=0xe6fff8)
                    await ctx.send(embed=embed)
                    return

            if info == 'random':
                data = await ses.get('https://disapi.ru/anime/random')
                data = await data.json()
            
            else:
                data = await ses.get(f'https://disapi.ru/anime/{inf}/{id}')
                if data.status != 200:
                    return
                data = await data.json()

            episode_length = data['episode_length_ru']

            if data['genres_ru']:
                genres_ru = ''
                for x in data['genres_ru']:
                    genres_ru += f'{x}, '
                genres_ru = genres_ru[:-2]

            episodes = data['episodes']
            licensed = data['licensed']
            name_ru = data['name_ru']
            poster = data['poster']
            rating = data['rating']
            type = data['type_ru']
            year = data['year']
            studio = data['studio']

            text = ''
            if type:
                text += f'Тип: `{type}`\n'
            
            if episodes:
                text += f'Эпизоды: `{episodes}`\n'

            if episode_length:
                text += f'Длительность эпизода: `{episode_length}`\n'

            if year:
                text += f'Год выхода: `{year}`\n'

            if data['genres_ru']:
                text += f'Жанры: `{genres_ru}`\n'
            
            if rating:
                text += f'Рейтинг: `{rating}`\n'

            if studio:
                text += f'Студия: `{studio}`\n'

            if licensed:
                text += f'Лицензировано: `{licensed}`\n'

            text = text[:-1]
                
            embed = discord.Embed(title = name_ru, description = text, color=0xe6fff8)
            embed.set_image(url=poster)
            await ctx.send(embed=embed)

    @commands.command()
    async def findanime(self, ctx, *,info = None):
        async with aiohttp.ClientSession() as ses:
            if info is None:
                embed = discord.Embed(description = '**Пример команды:**\n` -findanime (название аниме) `', color=0xe6fff8)
                await ctx.send(embed=embed)
                return
            
            embed = discord.Embed(description = 'Поиск...', color=0xe6fff8)
            msg = await ctx.send(embed=embed)
            data = await ses.get(f'https://disapi.ru/anime/find/ru/{info}')
            data = await data.json()
            data = data['top_1']
            episode_length = data['episode_length_ru']

            if data['genres_ru']:
                genres_ru = ''
                for x in data['genres_ru']:
                    genres_ru += f'{x}, '
                genres_ru = genres_ru[:-2]

            episodes = data['episodes']
            licensed = data['licensed']
            name_ru = data['name_ru']
            poster = data['poster']
            rating = data['rating']
            type = data['type_ru']
            year = data['year']
            studio = data['studio']

            text = ''
            if type:
                text += f'Тип: `{type}`\n'
            
            if episodes:
                text += f'Эпизоды: `{episodes}`\n'

            if episode_length:
                text += f'Длительность эпизода: `{episode_length}`\n'

            if year:
                text += f'Год выхода: `{year}`\n'

            if data['genres_ru']:
                text += f'Жанры: `{genres_ru}`\n'

            if rating:
                text += f'Рейтинг: `{rating}`\n'

            if licensed:
                text += f'Лицензировано: `{licensed}`\n'

            if studio:
                text += f'Студия: `{studio}`\n'

            text = text[:-1]

            await msg.delete()
                
            embed = discord.Embed(title = name_ru, description = text, color=0xe6fff8)
            embed.set_image(url=poster)
            await ctx.send(embed=embed)


    @commands.command()
    async def findhentai(self, ctx, *,info = None):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as ses:
                if info is None:
                    embed = discord.Embed(description = '**Пример команды:**\n` -findhentai (название хентая) `', color=0xe6fff8)
                    await ctx.send(embed=embed)
                    return
                
                embed = discord.Embed(description = 'Поиск...', color=0xe6fff8)
                msg = await ctx.send(embed=embed)
                data = await ses.get(f'https://disapi.ru/hentai/find/{info}')
                data = await data.json()
                data = data['top_1']

                if data['genres']:
                    genres = ''
                    for x in data['genres']:
                        genres += f'{x}, '
                    genres = genres[:-2]

                episodes = data['episodes']
                name = data['name']
                poster = data['poster']
                year = data['year']
                studio = data['studio']
                censored = data['censored']

                text = ''
                if censored == True:
                    text += f'Цензура: `Присутствует`\n'

                if censored == False:
                    text += f'Цензура: `Отсутствует`\n'

                if episodes:
                    text += f'Эпизоды: `{episodes}`\n'

                if year:
                    text += f'Год выхода: `{year}`\n'

                if studio:
                    text += f'Студия: `{studio}`\n'

                if data['genres']:
                    text += f'Жанры: `{genres}`\n'

                text = text[:-1]

                await msg.delete()
                    
                embed = discord.Embed(title = name, description = text, color=0xe6fff8)
                embed.set_image(url=poster)
                await ctx.send(embed=embed)

        else:
            embed = discord.Embed(description = '💢Канал не является NSFW-каналом', color=0xe6fff8)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(User(client))