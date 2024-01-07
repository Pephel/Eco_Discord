from typing import Optional

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", help_command=None, intents=discord.Intents.all())

TOKEN = ""        

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

class MyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)  # times out after 30 seconds
        button = discord.ui.Button(label='Московское', style=discord.ButtonStyle.url, url='https://voop.eco/')
        self.add_item(button)

        button2 = discord.ui.Button(label='СПБ', style=discord.ButtonStyle.url, url='https://ecopeterburg.ru/')
        self.add_item(button2)        

        button3 = discord.ui.Button(label='Воронеж', style=discord.ButtonStyle.url, url='https://eco.voronezh-city.ru/glavnaya/')
        self.add_item(button3)

        button4 = discord.ui.Button(label='Бесплатный код без смс регистрации', style=discord.ButtonStyle.url, url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        self.add_item(button4)

    async def on_timeout(self):
        # set the view to None so that the buttons are no longer available
        # or you could just disable the buttons if you want
        await self.message.edit(content="Link timed out", view=None)        

@bot.command()
async def list(ctx):
    await ctx.send("Список:", view = MyView())   

    
bot.run(TOKEN)