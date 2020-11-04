#import math
import random
import _asyncio

import discord
import praw
from discord.ext import commands


Client = discord.Client()
bot = commands.Bot(command_prefix = ";")


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

@bot.event
async def on_message(ctx):
	if ctx.content == "ueli":
		await ctx.channel.send("HOW DARE YOU MENTION THE FORBIDDEN ONE!")
        #await client.process_commands(ctx)

#@client.event
#async def on_message(ctx):
    #if "ueli" in ctx.content:
        #emoji = "\N{UELIGODHAND}"
        #await ctx.add_reaction(emoji)

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
    embed.set_author(name='Help : list of commands available')
    embed.add_field(name=';ping', value='Returns bot respond time in milliseconds', inline=False)
    embed.add_field(name=';quote', value='Get inspired by a powerful quote', inline=False)
    embed.add_field(name=';8ball', value='Ask the magic 8ball a question', inline=False)
    embed.add_field(name=';sum', value='Add to numbers togheter: ;sum 3 8', inline=False)
    embed.add_field(name=';multi', value='Multiply two numbers togheter: ;multi 3 8', inline=False)
    embed.add_field(name=';dank', value='Sends a random meme from r/dankmemes', inline=False)
    embed.add_field(name=';okbr', value='Sends a random meme from r/okbuddyretard', inline=False)
    embed.add_field(name=';cursed', value='Sends a random meme from r/cursedimages', inline=False)
    embed.add_field(name=';meme <subreddit<', value='Sends a random post from a subreddit of your choice!', inline=False)
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
    post_to_pick = random.randint(1, 50)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)

@bot.command()
async def okbr(ctx):
    memes_submissions = reddit.subreddit('okbuddyretard').hot()
    post_to_pick = random.randint(1, 50)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)

@bot.command()
async def cursed(ctx):
    memes_submissions = reddit.subreddit('cursedimages').hot()
    post_to_pick = random.randint(1, 50)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)

@bot.command()
async def meme(ctx, subreddit=None):
    if subreddit is None:
        memes_submissions = reddit.subreddit('dankmemes').hot()
    #message = None
    else: memes_submissions = reddit.subreddit(subreddit).hot()
    post_to_pick = random.randint(1, 50)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    if submission.over_18:
        user = ctx.message.author.mention
        await ctx.send(f'Oh {user}, you naughty naughty :smirk:')
    else:
        await ctx.send(submission.url)

with open("TOKEN.txt") as f:
  token = f.read()
bot.run(token)



