import nextcord, requests
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions

class Fox(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Connect To Affirmation API
    @commands.command(pass_context=True)
    async def fox(self, ctx):
        response = requests.get("https://randomfox.ca/floof/")
        fox = response.json()
        foxEmbed = nextcord.Embed(
            title="Enjoy your Fox 🦊",
            description=f"{fox['link']} \n\nRequested By <@{ctx.author.id}>",
            url=f"",
            color=0x2852fa
        )
        foxEmbed.set_image(url=f"{fox['image']}")
        await ctx.send(embed=foxEmbed)

# Setup
def setup(client):
    client.add_cog(Fox(client))