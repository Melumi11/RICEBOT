import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='~', intents = intents)

rices = os.listdir('rice')
ricedishess = os.listdir('ricedishes')

@bot.event
async def on_ready():
    print('A C T I V A T I O N N N N N')
    #print(random.choice(rices))
    #this works but sending the image doesn't

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    await bot.process_commands(message)

@bot.command(
  help = "If you want to ask, \"So er...What do you do?\"",
  brief = "I answer your question."
)
async def whatdo(message):
  await message.channel.send('R I C E B O T  H A S  T W O  P U R P O S E S: \nC O O K  B E S T  R I C E \nA N D  E M O T I O N A L  S U P P O R T')

@bot.command(
  help = "If you're feeling hungry.",
  brief = "I give you a rice dish."
)
async def ricedish(message):
  await message.channel.send(file = discord.File(random.choice(ricedishess)))

@bot.command(
  help = "If you want rice.",
  brief = "R I C E"
)
async def wantrice(message):
  await message.channel.send(file = discord.File(random.choice(rices)))

bot.run(os.getenv("TOKEN"))
