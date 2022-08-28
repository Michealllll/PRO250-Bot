import nextcord, requests, unittest
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions

class Quote(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Connect To Quote API
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

# Unit Testing
class TestQuoteAPIConnection_Success(unittest.TestCase):
    def testResponse_Success(self):
        response = requests.get("https://zenquotes.io/api/quotes")
        self.assertEqual(response.status_code, 200)

class TestQuoteAPIConnection_Failure(unittest.TestCase):
    def testResponse_Failure(self):
        response = requests.get("https://zenquotes.io/api/quotes")
        self.assertNotEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()