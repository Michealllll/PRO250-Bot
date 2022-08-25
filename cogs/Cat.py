import nextcord, requests
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions
# https://http.cat/[status_code]

#response = requests.get("https://http.cat/[num starting at 100]")
#print(response.text)





# affirmation = response.json()




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


# Setup
def setup(client):
    client.add_cog(Cat(client))
