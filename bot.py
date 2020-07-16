import os
import discord
from discord.ext import commands
import random

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='9k')

@bot.event
async def on_ready():
    #guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    #guild = discord.utils.get(bot.guilds, name=GUILD)   

    print(
        f'{bot.user.name} has connected to discord:\n'
        #f'{guild.name}(id: {guild.name})'
        )

    #members = '\n - '.join([member.name for member in guild.members])
    #print(f'Guild Members:\n - {members}')

#member joining
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Smoke grass {member.name}, welcome to hell'
    )
    print(f'messaged:\n - {member.name}')

@bot.command(name="test", help='smokes you')
async def on_message(ctx):
    liners = ['get toasted']
    response = random.choice(liners)
    await ctx.send(response)

@bot.command(name="peener", help='changes nickname')
async def change_name(ctx, member: discord.Member):
    await member.edit(nick='peener')
    print("name change\n")
        
@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhadled message: {args[0]}\'n')
        else:
            raise


bot.run(TOKEN)
