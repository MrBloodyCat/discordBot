import discord
from discord.ext import commands
import json
import os


with open('config.json', 'r') as file:
	config = json.load(file)


intents = discord.Intents.all()


client = commands.Bot(command_prefix = config["settings"]["prefix"], intents = intents)
client.remove_command("help")


@client.command()
@commands.is_owner()
async def load(ctx, extension):
	client.load_extension(f"cogs.{extension}")


@client.command()
@commands.is_owner()
async def unload(ctx, extension):
	client.unload_extension(f"cogs.{extension}")


@client.command()
@commands.is_owner()
async def reload(ctx, extension):
	client.unload_extension(f"cogs.{extension}")
	client.load_extension(f"cogs.{extension}")


for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f"cogs.{filename[:-3]}")

client.run(config["settings"]["token"])
