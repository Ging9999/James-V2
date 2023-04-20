from onoff import Run, Off
from discord.ext import commands
import discord


class Client(commands.Bot):
    def __init__(self, cmdprf: str, dcIntents : discord.Intents):
        super().__init__(command_prefix= cmdprf, intents = dcIntents())
    
    async def on_ready(self):
        print('{client.user.name} is ready to go!')
    async def on_message(self, message : discord.Message):
        if message.author.bot : return

        if self.user.mentioned_in(message=message) and "/Off" in message.content.lower():
            Off()

Run()







