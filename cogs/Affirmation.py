import nextcord, requests, unittest
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions

class Affirmation(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Connect To Affirmation API
    @commands.command(pass_context=True)
    async def affirmation(self, ctx):
        response = requests.get("https://www.affirmations.dev/")
        affirmation = response.json()
        affEmbed = nextcord.Embed(
            title="Enjoy your Randomized Affirmation",
            description=f"{affirmation['affirmation']} \n\nRequested By <@{ctx.author.id}>",
            url=f"",
            color=0x2852fa
        )
        await ctx.send(embed=affEmbed)

# Setup
def setup(client):
    client.add_cog(Affirmation(client))




# Unit Testing
class TestAffirmation(unittest.TestCase):
    def testResponse(self):
        self.assertIsNotNone == True

if __name__ == '__main__':
    unittest.main()