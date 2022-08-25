import nextcord, requests
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions

class Quote(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Connect To Joke API
    @commands.command(pass_context=True)
    async def quote(self, ctx):
        response = requests.get("https://zenquotes.io/api/quotes")
        quote = response.json()

        
        quoEmbed = nextcord.Embed(
            title=f"\"{quote[0]['q']}\"",
            description=f"Quote author: {quote[0]['a']} \n\nRequested By <@{ctx.author.id}>",
            url=f"",
            color=0x2852fa
        )
        await ctx.send(embed=quoEmbed)

# Setup
def setup(client):
    client.add_cog(Quote(client))