<<<<<<< HEAD
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
=======
import nextcord
from nextcord.ext import commands


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Help command
    @nextcord.slash_command(guild_ids=[977477205573652518], description="Help Command")
    async def help(self, interaction: nextcord.Interaction):
        embed = nextcord.Embed(
            title="Commands",
            color=0x2852fa,
            description=f"-Help - Display This Message \n-Ban [Member] [Reason] - Ban A Spesific Member From The Server \n-Kick [Member] [Reason] - Kick A Spesific Member\n-YtSearch [Query] - Search On Youtube For Query \n-GSearch [Query] - Search On Google For Query \n-Myid - Tell You Your Id \n-Lyrics [Artist] [Song] - Search For A Song's Lyrics By Artist \n-YesOrNo [Question] - Ask The Bot A Question \n-CheckMcName [Name] - Check If A Minecraft Name Is Availbe Or Not \n-GetId [Member] - Get The Id Of A Member And Send It\n-Play [Song Url] - Play The Song From The Youtube Url\n-Stop - Stop The Song That's Currently Playing"
        )
        await interaction.response.send_message(embed=embed)


# setup
def setup(client):
    client.add_cog(Help(client))
>>>>>>> a9e3e83f4a3e1cd2a8fb46e7eaa785f225dcfd5c
