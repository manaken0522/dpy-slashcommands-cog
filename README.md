# dpy-slashcommands-cog
Using slash commands in discord.py cogs

# Example
cogs/commands/example.py:
```python
import discord
from discord.ext import commands

class example(commands.Cog):
    def __init__(self, client):
        self.client = client

    @discord.app_commands.command(name='example', description='example command')
    async def ping(self, interaction:discord.Interaction):
        await interaction.response.send_message('example response')

async def setup(client:commands.Bot):
    await client.add_cog(example(client))
```
