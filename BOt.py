import random
import discord
from discord.ext import commands


Client = discord.Client()
client = commands.Bot(command_prefix = "m!")


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('m!help for a list of Commands'))
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

@client.event
async def on_member_remove(member):
    print (f'{member} just left our Server. He got smol pp now :(')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases =['8ball', 'questions'])
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
@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'Error. Try !help ({error})')

#Answers with a random quote
@client.command()
async def quote(ctx):
    responses = open('quotes.txt').read().splitlines()
    random.seed(a=None)
    response = random.choice(responses)
    await ctx.send(response)

#delete default help command
client.remove_command("help")

#Embeded help with list and details of commands
@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.green())
    embed.set_author(name='Help : list of commands available')
    embed.add_field(name='m!ping', value='Returns bot respond time in milliseconds', inline=False)
    embed.add_field(name='m!quote', value='Get inspired by a powerful quote', inline=False)
    embed.add_field(name='m!8ball', value='Ask the magic 8ball a question', inline=False)
    await ctx.send(embed=embed)

with open("TOKEN.txt") as f:
  token = f.read()
client.run(token)



