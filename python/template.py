import discord
from discord.ext import commands
import random

intents = discord.Intents.all()
client = commands.Bot(command_prefix='.', intents=intents)


@client.event
async def on_ready():
    print(f'logged in as {client.user}')


coinflip = ['Heads', 'Tails']

Sentences = [
    'Hello, im Jack.', "I Hate you.", "You look nice today.",
    "Can you help me?", "Im a very funny guy.", "You look like a rotten egg.",
    "Fuck You.", "Can I Help You.", "You look like a dumbass."
]

YoMamaJokes = [
    "Yo mama so poor when I saw her kicking a can down the street, I asked her what she was doing, she said Moving.",
    "Yo mama so skinny when she swallowed a meatball everyone thought she was pregnant again.",
    "Yo mama so ugly even Hello Kitty said good bye.",
    "Yo mama so ugly when she looks in the mirror her reflection ducks.",
    "Yo mama so fat she uses Google Earth to take a selfie.",
    "Yo mama so poor she went to McDonald's and put a milkshake on layaway."
]

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.coinflip'):
        await message.channel.send(random.choice(coinflip))

    if message.content.startswith('.yomama'):
        await message.channel.send(random.choice(YoMamaJokes))

    if message.content.startswith('.respond'):
        await message.channel.send(random.choice(Sentences))



client.run('YOUR TOKEN HERE')
