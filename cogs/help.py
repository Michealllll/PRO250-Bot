import nextcord
from nextcord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Help command
    @commands.command(pass_context=True)
    async def help(self, ctx):
        embed = nextcord.Embed(
            title=f"Commands for <@{ctx.author.id}>",
            color=0x2852fa,
            description=f",Help - Display This Message \n ,affirmation - Responds with randomized Affirmation \n ,cat - Responds with randomized Cat Picture \n ,checkmcname [name] - Responds with a link to namemc with your search result \n ,fox - Responds with randomized Fox Picture \n ,getid [discord username] - Responds with requested users Discord ID \n ,help - Display This Message \n ,joke - Responds with randomized Yo Momma Joke \n ,play [song name] - Bot will search YouTube for the top search result according to input, and play it in your voice channel. \n ,pause - Pauses the music being played from the Bot. \n ,resume - Resumes the music if Paused. \n ,stop - Stops the Bot from playing the currently Playing search. This removes the search from the track. \n ,myid - Responds with the your Discord ID. \n ,quote - Responds with randomized Quote off the internet. \n ,ruser - Responds with Random/False Personal Information about You."
        )
        await ctx.send(embed=embed)


# setup
def setup(client):
    client.add_cog(Help(client))
