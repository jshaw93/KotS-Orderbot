import discord
from discord import app_commands
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = discord.Object(id=int(os.getenv('DISCORD_GUILD')))


class Client(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=GUILD)
        await self.tree.sync(guild=GUILD)

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return


_intents = discord.Intents.default()
_intents.message_content = True
client = Client(intents=_intents)


@client.tree.command(
    name="order",
    description="Order a craft from a selected category"
)
async def order(ctx: discord.Interaction):
    pass
