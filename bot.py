import os
import yaml
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

config = None
if os.path.isfile("config.yaml"):
    with open("config.yaml") as config_file:
        config = yaml.load(config_file)
else:
    exit("No configuration file 'config.yaml' found")
    sys.exit()


Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Bot is online and connected to Discord")

@client.event
async def on_message(message):
  userID = message.author.id
  if message.content.upper().startswith('!PING'):
    await client.send_message(message.channel, "<@%s> Pong!" % (userID))

  if message.content.lower().startswith('/commands'):
    msg = config['commands']
    await client.send_message(message.channel, msg)

  if message.content.lower().startswith('/extras'):
    msg = config['extras']
    await client.send_message(message.channel, msg)

  if message.content.lower().startswith('/community'):
    msg = config['community']
    await client.send_message(message.channel, msg)

  if message.content.lower().startswith('/resources'):
    msg = config['resources']
    await client.send_message(message.channel, msg)

  if message.content.lower().startswith('/conferences'):
    msg = config['conferences']
    await client.send_message(message.channel, msg)

  if message.content.lower().startswith('/previousevents'):
    msg = config['previousevents']
    await client.send_message(message.channel, msg)

  if message.content.lower().startswith('/videos'):
    msg = config['videos']
    await client.send_message(message.channel, msg)

  if message.content.lower().startswith('/uraiden'):
    msg = config['uraiden']
    await client.send_message(message.channel, msg)

  if message.content.lower().startswith('/whenmoon'):
    msg = config['whenmoon']
    await client.send_message(message.channel, msg)

  if message.content.lower().startswith('/rules'):
    msg = config['rules']
    await client.send_message(message.channel, msg)

  if message.content.lower().startswith('/pulse'):
    msg = config['pulse']
    await client.send_message(message.channel, msg)

  if message.content.lower().startswith('/nightly'):
    msg = config['nightly']
    await client.send_message(message.channel, msg)

  if message.content.lower().startswith('/release'):
    msg = config['release']
    await client.send_message(message.channel, msg)

  if message.content.lower().startswith('/email'):
    msg = config['email']
    await client.send_message(message.channel, msg)

  if message.content.lower().startswith('/brainbot'):
    msg = config['brainbot']
    await client.send_message(message.channel, msg)

  if message.content.lower().startswith('/tokenmodel'):
    msg = config['tokenmodel']
    await client.send_message(message.channel, msg)

  if message.content.lower().startswith('/disclaimer'):
    msg = config['disclaimer']
    await client.send_message(message.channel, msg)

  if message.content.lower().startswith('/rapps'):
    msg = config['rapps']
    await client.send_message(message.channel, msg)

  if message.content.lower().startswith('/mentions'):
    msg = config['mentions']
    await client.send_message(message.channel, msg)

client.run("TOKEN")
