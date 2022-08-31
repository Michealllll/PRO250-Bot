<<<<<<< HEAD
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
class TestAffirmationAPI_Success(unittest.TestCase):
    def testResponse_Success(self):
        response = requests.get("https://www.affirmations.dev/")
        self.assertEqual(response.status_code, 200)

class TestAffirmationAPI_Failure(unittest.TestCase):
    def testResponse_Failure(self):
        response = requests.get("https://www.affirmations.dev/")
        self.assertNotEqual(response.status_code, 404)

if __name__ == '__main__':
=======
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
class TestAffirmationAPI_Success(unittest.TestCase):
    def testResponse_Success(self):
        response = requests.get("https://www.affirmations.dev/")
        self.assertEqual(response.status_code, 200)

class TestAffirmationAPI_Failure(unittest.TestCase):
    def testResponse_Failure(self):
        response = requests.get("https://www.affirmations.dev/")
        self.assertNotEqual(response.status_code, 404)

if __name__ == '__main__':
>>>>>>> a9e3e83f4a3e1cd2a8fb46e7eaa785f225dcfd5c
    unittest.main()