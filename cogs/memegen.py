import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions


class MemeGen(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Connect To MemeGenerator API

# Setup
def setup(client):
    client.add_cog(MemeGen(client))
