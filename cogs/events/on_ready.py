from discord.ext import commands

class on_ready(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('起動完了')
        await self.client.tree.sync()

async def setup(client:commands.Bot):
    await client.add_cog(on_ready(client))