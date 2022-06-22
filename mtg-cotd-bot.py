#!/usr/bin/python

import scrython
import time
import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

card = scrython.cards.Random()
print(card.image_uris()['normal'])
