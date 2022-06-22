# the-spy-bot.py
# Basic bot created by following a Discord Bot Tutorial on RealPython.com. 
# https://realpython.com/how-to-make-a-discord-bot-python/#connecting-a-bot
#  

#!/usr/bin/python

import os
from urllib import response
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Defines the prefix that indicates a command is being run.
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
      f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_member_join(member):
  await member.create_dm()
  await member.dm_channel.send(
    f'Greetings {member.name}, wecome to {GUILD}.')

@bot.event
async def on_message(message):

  laughter = [
    'HA HA. I am laughing. HA HA',
    'LOLZ',
    'TEE HEE'
  ]

  if message.content == 'lol':
    response = random.choice(laughter)
    await message.channel.send(response)

@bot.command(name="roll_dice", help="Simulates rolling dice.")
async def roll(ctx, number_of_dice: int, number_of_sides: int):
  dice = [
    str(random.choice(range(1, number_of_sides + 1)))
    for _ in range(number_of_dice)
  ]
  await ctx.send(', '.join(dice))

bot.run(TOKEN)