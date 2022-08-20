import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions


class Cat(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Connect To Cat Image API

# Setup
def setup(client):
    # client.add_cog(Kick(client))
