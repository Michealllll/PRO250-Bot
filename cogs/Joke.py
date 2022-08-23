import nextcord, requests
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions



class Joke(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Connect To Joke API
    @commands.command(pass_context=True)
    async def joke(self, ctx):
        response = requests.get("https://yomomma-api.herokuapp.com/jokes")
        joke = response.json()
        affEmbed = nextcord.Embed(
            title="Enjoy your Randomized Yo Momma Joke",
            description=f"{joke['joke']} \n\nRequested By <@{ctx.author.id}>",
            url=f"",
            color=0x2852fa
        )
        await ctx.send(embed=affEmbed)

# Setup
def setup(client):
    client.add_cog(Joke(client))
