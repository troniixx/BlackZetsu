#import math
import random

import aiohttp
import asyncio
import logging
import gc
import sys
import random
import re
import aiohttp


import discord
import praw
from discord.ext import commands


Client = discord.Client()
#bot = commands.Bot(command_prefix = ";")

log = logging.getLogger('LOG')

bot = commands.Bot(command_prefix=';', description="Second half of white Zetsu")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Second half of white Zetsu",  color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    #embed.set_thumbnail(url=f"{ctx.guild.icon}")

    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(';help for a list of Commands'))
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))

@bot.event
async def on_member_remove(member):
    print (f'{member} just left our Server. He got smol pp now :(')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

@bot.command()
async def madara(ctx):
    await ctx.send('Wake up to reality. Nothing ever goes as planned in this world. The longer you live,the more you realize that only pain, suffering and futility exists in this reality.')

@bot.command()
async def sum(ctx, numOne: float, numTwo: float):
    await ctx.send(numOne + numTwo)

@bot.command()
async def multi(ctx, numOne: float, numTwo: float):
    await ctx.send(numOne * numTwo)


@bot.command(aliases =['8ball', 'questions'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

#If there is an error, it will answer with an error
#@client.event
#async def on_command_error(ctx, error):
    #await ctx.send(f'Error. Try !help ({error})')


#Answers with a random quote
@bot.command()
async def quote(ctx):
    responses = open('quotes.txt').read().splitlines()
    random.seed(a=None)
    response = random.choice(responses)
    await ctx.send(response)

#delete default help command
bot.remove_command("help")

#Embeded help with list and details of commands
@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.green())
    embed.set_author(name='Help : list of commands available.')
    embed.add_field(name=';ping', value='Returns bot respond time in milliseconds', inline=False)
    embed.add_field(name=';madara', value='Inspire yourself to find reason in this world', inline=False)
    embed.add_field(name=';info', value='Random info stuff', inline=False)
    embed.add_field(name=';quote', value='Get inspired by a powerful quote', inline=False)
    embed.add_field(name=';8ball', value='Ask the magic 8ball a question', inline=False)
    embed.add_field(name=';sum', value='Add to numbers togheter: ;sum 3 8', inline=False)
    embed.add_field(name=';multi', value='Multiply two numbers togheter: ;multi 3 8', inline=False)
    embed.add_field(name=';dank', value='Sends a random meme from r/dankmemes', inline=False)
    embed.add_field(name=';okbr', value='Sends a random meme from r/okbuddyretard', inline=False)
    embed.add_field(name=';cursed', value='Sends a random meme from r/cursedimages', inline=False)
    embed.add_field(name=';tsundere', value='Sends a beautiful tsundere from r/Tsunderes', inline=False)
    embed.add_field(name=';waifu', value='Sends a hot 2D waifu from r/AnimeGirls', inline=False)
    embed.add_field(name=';moe', value='Just trust me on that one ;)', inline=False)
    embed.add_field(name=';meme <subreddit>', value='Sends a random post from a subreddit of your choice!', inline=False)
    await ctx.send(embed=embed)

#reddit random meme
f=open("clientid.txt", "r")
if f.mode == 'r':
    clientid = f.read()

f=open("clientsecret.txt", "r")
if f.mode == 'r':
    clientsec = f.read()

reddit = praw.Reddit(client_id = clientid,
                     client_secret= clientsec,
                     user_agent='Discord Bot by /u/TroNiiXx'
                     'https://github.com/troniixx/DiscordBot')

@bot.command()
async def dank(ctx):
    memes_submissions = reddit.subreddit('dankmemes').hot()
    post_to_pick = random.randint(1, 45)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    await ctx.send(submission.url)

@bot.command()
async def okbr(ctx):
    memes_submissions = reddit.subreddit('okbuddyretard').hot()
    post_to_pick = random.randint(1, 45)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)

@bot.command()
async def cursed(ctx):
    memes_submissions = reddit.subreddit('cursedimages').hot()
    post_to_pick = random.randint(1, 45)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)

@bot.command()
async def meme(ctx, subreddit=None):
    if subreddit is None:
        memes_submissions = reddit.subreddit('dankmemes').hot()
    #message = None
    else: memes_submissions = reddit.subreddit(subreddit).hot()
    post_to_pick = random.randint(1, 45)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)

@bot.command()
async def tsundere(ctx):
    memes_submissions = reddit.subreddit('Tsunderes').hot()
    post_to_pick = random.randint(1, 45)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)

@bot.command()
async def waifu(ctx):
    memes_submissions = reddit.subreddit('AnimeGirls').hot()
    post_to_pick = random.randint(1, 45)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)

@bot.command()
async def moe(ctx):
    memes_submissions = reddit.subreddit('NoneHumanMoe').hot()
    post_to_pick = random.randint(1, 45)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    #if submission.over_18:
        #user = ctx.message.author.mention
        #await ctx.send(f'Oh {user}, you naughty naughty :smirk:')
    #else:
    await ctx.send(submission.url)


with open("TOKEN.txt") as f:
  token = f.read()
bot.run(token)




#dumb shit part 2







