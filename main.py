import os
import asyncio
import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix=None, intents=intents)

#loading extensions
async def load_extension():
    for type in ['commands', 'events']:
        cogs = os.listdir(f'./cogs/{type}/')
        for cog in cogs:
            # __pycache__やpythonスクリプトじゃないファイルサイズが0のファイルを除外
            if cog[0:2] != '__' and cog[-3:] == '.py' and os.path.getsize(f'./cogs/{type}/{cog}') != 0:
                cog = cog.replace('.py', '')
                await client.load_extension(f'cogs.{type}.{cog}')

async def main():
    await load_extension()
    await client.start('set your application token here')

asyncio.run(main())