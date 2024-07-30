import discord
from discord.ext import tasks

intents = discord.Intents.default()
intents.members = True  

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Бот запущен как: {client.user}')
    update_status.start() 

@tasks.loop(seconds=10) 
async def update_status():
    guild = discord.utils.get(client.guilds)  
    if guild:
        member_count = guild.member_count  
        await client.change_presence(activity=discord.Game(f'{member_count} участников'))

client.run('Ваш токен')
