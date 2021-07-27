# Required dependencies
import discord
from discord.ext import commands
import requests
import json



#import bot token
from apikeys import *

intents = discord.Intents.default()
intents.members = True

client = commands.Bot( command_prefix = '!', intents=intents)

@client.event
async def on_ready():
    print("* * * * * * * * * * * * * * * * * * * * * *")
    print("* * * * * SludgeBot is now online * * * * *")
    print("* * * * * * * * * * * * * * * * * * * * * *")

# This is what the user will type into the chat to call certain action from the bot.

@client.command() 
async def hello(ctx):
    await ctx.send("...Greetings. I am SludgeBot.")

@client.command()
async def goodbye(ctx):
    await ctx.send("...Farewell, human. ")

@client.event
async def on_member_join(member):

    jokeurl = "http://joke3.p.rapidapi.com/v1/joke"

    headers = {
        'x-rapidapi-key': JOKEAPI,
        'x-rapidapi-host': "joke3.p.rapidapi.com"
        }

    response = requests.request("GET", jokeurl, headers=headers)

    channel = client.get_channel(866084281016647693)
    await channel.send("...Welcome, Human.")
    await channel.send(json.loads(response.text)['content'])

@client.event 
async def on_member_remove(member):


    channel = client.get_channel(866084281016647693)
    await channel.send("...Farewell, human. ")

client.run(BOTTOKEN)