import nextcord, wavelink
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions

class Music(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client
        client.loop.create_task(self.node_connect())

    async def node_connect(self):
        await self.client.wait_until_ready()
        await wavelink.NodePool.create_node(bot=self.client, host='lavalinkinc.ml', port=443, password='incognito', https=True)

    @commands.Cog.listener()
    async def on_wavelink_node_ready(self, node: wavelink.Node):
        print(f'Wavelink Node <{node.identifier}> is ready!')

    @commands.command()
    async def play(self, ctx: commands.Context, *, search: wavelink.YouTubeTrack):
        if not ctx.voice_client:
            vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
        else:
            vc: wavelink.Player = ctx.voice_client

        await vc.play(search)

        # playEmbed = nextcord.Embed(
        #     title=f"{search['title']}",
        #     description=f"{search['title']} \n\nRequested By <@{ctx.author.id}>",
        #     url=f"",
        #     color=0x2852fa
        # )
        # await ctx.send(embed=playEmbed)

# Setup
def setup(client):
    client.add_cog(Music(client))
