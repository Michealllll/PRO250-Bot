import nextcord, requests
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions

response = requests.get("http://api.forismatic.com/api/1.0/")
quote = response.json()
print(quote)

class Quote(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Connect To Joke API
#     @commands.command(pass_context=True)
#     async def quote(self, ctx):
#         response = requests.get("http://api.forismatic.com/api/1.0/")
#         quote = response.json()
#         #print(quote)
#         quoEmbed = nextcord.Embed(
#             title="Enjoy your Randomized Yo Momma Joke",
#             description=f"{quote['joke']} \n\nRequested By <@{ctx.author.id}>",
#             url=f"",
#             color=0x2852fa
#         )
#         await ctx.send(embed=quoEmbed)

# # Setup
# def setup(client):
#     client.add_cog(Quote(client))