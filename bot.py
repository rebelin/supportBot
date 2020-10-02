import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from random import choice

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
bot = commands.Bot(command_prefix=".")

encouragementFile = 'wordsOfEncouragement.txt'
with open(encouragementFile,'r') as f:
    encouragementList = f.readlines()

adviceFile = 'wordsOfAdvice.txt'
with open(adviceFile,'r') as f:
    adviceList = f.readlines()

inspirationalFile = 'inspirationalQuotes.txt'
inspirationList = []
with open(inspirationalFile,'r') as f:
    for line in f.readlines():
        quote, citation = line.split(';')
    inspirationList.append((quote, citation))

lessonFile = 'lifeLessons.txt'
with open(lessonFile, 'r' as f):
    lessonList = f.readlines()

# await bot.connect()

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
    guild = discord.utils.get(bot.guilds, name=GUILD)
    # print(
    #     f'{bot.user} has connected to Discord!\n'
    #     f'{guild.name}(id: {guild.id})'
    # )
    await bot.change_presence(status=discord.Status.online)

@bot.command(name='stop', help='Exit bot')
async def stop(ctx):
    await ctx.send('Bye, have a good one!')
    await bot.change_presence(status=discord.Status.offline)
    await bot.close()

@bot.command(name='encourage', help='Responds with words of encouragement')
async def encouragement(ctx):
    encouragement = choice(encouragementList)
    await ctx.send(encouragement)

@bot.command(name='advice', help='Responds with words of advice')
async def advice(ctx):
    advice = choice(adviceList)
    await ctx.send(advice)

@bot.command(name='inspire', help='Responds with an inspirational quote')
async def inspire(ctx):
    quote, citation = choice(inspirationList)
    await ctx.send(f'{quote}\n  - {citation}\n')

@bot.command(name='sendMessage', help='Sends a message to someone')
async def messenger(ctx, receiver: discord.User, type):
    if type == 'encourage':
        encouragement = choice(encouragementList)
        await receiver.send(encouragement)
    elif type == 'advice':
        advice = choice(adviceList)
        await receiver.send(advice)
    elif type == 'inspire':
        quote, citation = choice(inspirationList)
        await receiver.send(f'{quote}\n - {citation}\n')
    elif type == 'life':
        lesson = choice(lessonList)
        await receiver.send(lesson)
    # elif type == 'custom':
    #     await ctx.send(f'What message would you like to send {receiver}?\n')
    #
    #     def check_reply(m):
    #         return m.author == ctx.author
    #     try:
    #         msg = await bot.wait_for('message', check=check_reply, timeout=60.0)
    #     except asyncio.TimeoutError:
    #         await ctx.send('You took too long...')
    #     else:
    #         await receiver.send(f'{msg.content}\n   - {ctx.author}\n')

bot.run(TOKEN)
