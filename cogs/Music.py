import nextcord, wavelink, unittest
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

        await ctx.send(f"Now Playing {search.title}")
        await vc.play(search)

    @commands.command()
    async def pause(self, ctx: commands.Context):
        if not ctx.voice_client:
            return await ctx.send("Music not being played. Unable to Pause.")
        elif not getattr(ctx.author.voice, "channel", None):
            return await ctx.send("It is required that the user be in a voice channel to Pause.")
        else:
            vc: wavelink.Player = ctx.voice_client

        await ctx.send(f"Music Paused. By: {ctx.author.name}")
        await vc.pause()

    @commands.command()
    async def resume(self, ctx: commands.Context):
        if not ctx.voice_client:
            return await ctx.send("Music not being played. Unable to Resume.")
        elif not getattr(ctx.author.voice, "channel", None):
            return await ctx.send("It is required that the user be in a voice channel to Resume Playing.")
        else:
            vc: wavelink.Player = ctx.voice_client

        await ctx.send(f"Music Resumed. By: {ctx.author.name}")
        await vc.resume()

    @commands.command()
    async def stop(self, ctx: commands.Context):
        if not ctx.voice_client:
            return await ctx.send("Music not being played. Unable to Stop a Player.")
        elif not getattr(ctx.author.voice, "channel", None):
            return await ctx.send("It is required that the user be in a voice channel to Stop a Player.")
        else:
            vc: wavelink.Player = ctx.voice_client

        await ctx.send(f"Music Stopped. By: {ctx.author.name}")
        await vc.stop()
        
    @commands.command()
    async def disconnect(self, ctx: commands.Context):
        vc: wavelink.Player = ctx.voice_client
        await ctx.send(f"Bot Disconnecting. By: {ctx.author.name}")
        await vc.disconnect()


# Setup
def setup(client):
    client.add_cog(Music(client))