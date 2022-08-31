<<<<<<< HEAD
import nextcord, requests
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions




import unittest

class Cat(commands.Cog):
    def __init__(self, client):
        self.client = client
    

    @commands.command(pass_context=True)
    async def cat(self, ctx):
        api_key = 'live_oQxlCVcGsl3KBfVTLdTrj5WT9Jtv0nf8aEbOjwxGK0l4tJwzqZMxLaWc779aexvX'
        response = requests.get(f"https://api.thecatapi.com/v1/images/search?api_key={api_key}")
        catobj = response.json()
        catEmbed = nextcord.Embed(
            title="Enjoy your Randomized Cat",
            description=f"{catobj[0]['url']} \n\nRequested By <@{ctx.author.id}>",
            url=f"",
            color=0x2852fa           
        )
        catEmbed.set_image(url=f"{catobj[0]['url']}")
        await ctx.send(embed=catEmbed)


class catTest(unittest.TestCase):
    def testResponse_Success(self):
        api_key = 'live_oQxlCVcGsl3KBfVTLdTrj5WT9Jtv0nf8aEbOjwxGK0l4tJwzqZMxLaWc779aexvX'
        response = requests.get(f"https://api.thecatapi.com/v1/images/search?api_key={api_key}")
        self.assertEqual(response.status_code, 200)

    def testResponse_Failure(self):
        api_key = 'live_oQxlCVcGsl3KBfVTLdTrj5WT9Jtv0nf8aEbOjwxGK0l4tJwzqZMxLaWc779aexvX'
        response = requests.get(f"https://api.thecatapi.com/v1/images/search?api_key={api_key}")
        self.assertNotEqual(response.status_code, 404)


# Setup
def setup(client):
    client.add_cog(Cat(client))
=======
import nextcord, requests
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions




import unittest

class Cat(commands.Cog):
    def __init__(self, client):
        self.client = client
    

    @commands.command(pass_context=True)
    async def cat(self, ctx):
        api_key = 'live_oQxlCVcGsl3KBfVTLdTrj5WT9Jtv0nf8aEbOjwxGK0l4tJwzqZMxLaWc779aexvX'
        response = requests.get(f"https://api.thecatapi.com/v1/images/search?api_key={api_key}")
        catobj = response.json()
        catEmbed = nextcord.Embed(
            title="Enjoy your Randomized Cat",
            description=f"{catobj[0]['url']} \n\nRequested By <@{ctx.author.id}>",
            url=f"",
            color=0x2852fa           
        )
        catEmbed.set_image(url=f"{catobj[0]['url']}")
        await ctx.send(embed=catEmbed)


class catTest(unittest.TestCase):
    def testResponse_Success(self):
        api_key = 'live_oQxlCVcGsl3KBfVTLdTrj5WT9Jtv0nf8aEbOjwxGK0l4tJwzqZMxLaWc779aexvX'
        response = requests.get(f"https://api.thecatapi.com/v1/images/search?api_key={api_key}")
        self.assertEqual(response.status_code, 200)

    def testResponse_Failure(self):
        api_key = 'live_oQxlCVcGsl3KBfVTLdTrj5WT9Jtv0nf8aEbOjwxGK0l4tJwzqZMxLaWc779aexvX'
        response = requests.get(f"https://api.thecatapi.com/v1/images/search?api_key={api_key}")
        self.assertNotEqual(response.status_code, 404)


# Setup
def setup(client):
    client.add_cog(Cat(client))
>>>>>>> a9e3e83f4a3e1cd2a8fb46e7eaa785f225dcfd5c
