import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f"BOT is ready and logged in as {client.user}")