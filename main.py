import nextcord
import os
from nextcord.ext import commands

token = os.getenv('BOTTOKEN')  # gets the environment variable that is the bot token i made one

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True
client = commands.Bot(command_prefix='-', intents=intents, help_command=None, case_insensitive=True)


# useful code
@client.event
async def on_ready():
    await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="This Server"))
    print("The Bot Is Up And Running")
    print("-------------------------")


# Cogs
innitial_extensions = []

for i in os.listdir("cogs"):
    if i.endswith(".py"):
        innitial_extensions.append("cogs." + i[:-3])

if __name__ == "__main__":
    for extension in innitial_extensions:
        client.load_extension(extension)

client.run('MTAwOTYyODQ3NDM1NDQ0MjM0Mw.GAT7bB.Gk4OZ0APD3I3IE3eLwR1tifYZqN_f3seNz8E2g')  # runs the bot
