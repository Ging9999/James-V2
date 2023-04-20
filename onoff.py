import discord
from discord.ext.commands.bot import Bot
from discord.ext import commands
from botdetails import bottoken
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
def Run():
    client.run(bottoken)
    print("On")
def Off():
    client.close()
    print("Off")