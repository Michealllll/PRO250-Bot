import nextcord, requests, unittest
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions

class RandomUser(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Connect To RandomUser API
    @commands.command(pass_context=True)
    async def ruser(self, ctx):
        response = requests.get("https://randomuser.me/api/")
        rand = response.json()
        randEmbed = nextcord.Embed(
            title=f"Here is @{ctx.author.name}'s information",
            description=f"Name: {rand['results'][0]['name']['first']} {rand['results'][0]['name']['last']} \n Gender: {rand['results'][0]['gender']} \n Street: {rand['results'][0]['location']['street']['number']} {rand['results'][0]['location']['street']['name']} \n City: {rand['results'][0]['location']['city']} \n State: {rand['results'][0]['location']['state']} \n Country: {rand['results'][0]['location']['country']}",
            color=0x000
        )
        randEmbed.set_image(url=f"{rand['results'][0]['picture']['large']}")
        await ctx.send(embed=randEmbed)

# Setup
def setup(client):
    client.add_cog(RandomUser(client))

# Unit Testing
class TestRandomUserAPIConnection_Success(unittest.TestCase):
    def testResponse_Success(self):
        response = requests.get("https://randomuser.me/api/")
        self.assertEqual(response.status_code, 200)

class TestRandomUserAPIConnection_Failure(unittest.TestCase):
    def testResponse_Failure(self):
        response = requests.get("https://randomuser.me/api/")
        self.assertNotEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
