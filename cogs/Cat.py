import nextcord, requests
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions
# https://http.cat/[status_code]

#response = requests.get("https://http.cat/[num starting at 100]")
#print(response.text)



class Cat(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Connect To Cat Image API

# Setup
def setup(client):
    client.add_cog(Cat(client))
