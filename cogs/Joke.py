import nextcord, requests, unittest
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
            color=0x2852fa
        )
        await ctx.send(embed=affEmbed)

# Setup
def setup(client):
    client.add_cog(Joke(client))

# Unit Testing
class TestJokeAPIConnection_Success(unittest.TestCase):
    def testResponse_Success(self):
        response = requests.get("https://yomomma-api.herokuapp.com/jokes")
        self.assertEqual(response.status_code, 200)

class TestJokeAPIConnection_Failure(unittest.TestCase):
    def testResponse_Failure(self):
        response = requests.get("https://yomomma-api.herokuapp.net/jokes")
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
