from ast import alias
from http.client import responses

import os
import asyncio
import random
import discord                                             # It is a module
from discord.ext import commands , tasks
from itertools import cycle

import youtube_dl

from jinja2 import pass_context                            # discord.ext is a extension # we import command becouse a bot can have so many commands
status=cycle(['status1','status 2'])
intents=discord.Intents.all()
client = commands.Bot(command_prefix='.',intents=intents)  # client is a variable # prefix is use to call the commands
@client.event                                              # First Event of a client # Event is a piece of code 
async def on_ready():                                      # asyncronus Function on_ready which shows that bot is ready
                                                           # change_status.start()
    await client.change_presence(status=discord.Status.idle,activity=discord.Game('Hello There!'))
    print("Bot is Ready.")

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')                # F string

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')

@client.event
async def on_member_invite(member):
    print(f'{member} invited someone')

@client.command()                                          # we need parenthesis becouse there are couple of attributes for commands such as a whole that we can change
async def ping(ctx):                                       # Context is represented by CTX   # we need to name the function what you want your command to be.
    await ctx.send(f'Pong!{round(client.latency*1000)}ms') # When the command is run the bot will say pong

@client.command(aliases=['8ball','test'])                  # aliases is second name given to a data(value of one variable is assigned to another variabe)
async def ball(ctx,*,question):                            # * allow me to take multiple parameters as sort of multiple arguments 
    responses=['It is certain',
    'It is decidedly so','Without a doubt','Yes, definitely','You may rely on it','As I see it, yes','Most likely','Outlook good','Yes'
    'Signs point to yes','Reply hazy try again','Ask again later','Better not tell you now','Cannot predict now','Concentrate and ask again',
    'Dont count on it','My reply is no','My sources say no','Outlook not so good','Very doubtful']
    await ctx.send(f'Question : {question}\nAnswer : {random.choice(responses)}')

@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send('Please pass in all required arguments.')


@client.command()
# async def clear(ctx,amount=5):                            # If we didn't gaye the clear amount then it will clear the message of the mentioned amount
async def clear(ctx,amount:int):
    await ctx.channel.purge(limit=amount)                   # Purge means Remove

@clear.error
async def clear_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send('Please specify the amount of message to delet')

@client.command()
async def kick(ctx , member : discord.Member,*,reason=None):
                                                            # reason=['Not Following The Rules','Using abusive language']
    await member.kick(reason=reason)
    await ctx.send(f'kicked {member.mention}')

@client.command()
async def ban(ctx , member : discord.Member,*,reason=None): # * takes all the additional parameters #discord.Member we can mention the member on dicord server
                                                            # reason=['Not Following The Rules','Using abusive language']
    await member.ban(reason=reason)
                                                            # await ctx.send(f'Banned {member.name}#{member.discriminator}')
    await ctx.send(f'Banned {member.mention}')

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()                   #guild is use to provide a list of banned users
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user                               #we aree setting all the banned user in user(now user contain all the banned user name)
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"UnBanned: {user.mention}")
            return

@tasks.loop(seconds=60)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

client.run('OTkyNTA4OTc0MDI2OTg1NDky.GbpIQ6.DaMVYCzDvUU3jNr5MRSgin1TH3wm6c7iELJsCU')
# OTkzOTE3NTI2NDkwNzU1MDgy.G66686.dYSf4DonvO97LKyLjfe2E1_k-yzJnbk5B3g4P4 it is a token 