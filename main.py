#import neverSleep
import nextcord
from nextcord.ext import commands
import os
from config import TOKEN

client = commands.Bot(command_prefix = "!" , intents=nextcord.Intents.all(),case_insensitive=True)       
client.remove_command('help')
client.remove_command("purge")
initial_extensions = []

def cog_loader():
  for filename in os.listdir("./events"):
    if filename.endswith(".py"):
      initial_extensions.append("events."+ filename[:-3])
  for filename in os.listdir("./commands"):
    if filename.endswith(".py"):
      initial_extensions.append("commands."+ filename[:-3])
  for filename in os.listdir("./serverstats"):
    if filename.endswith(".py"):
      initial_extensions.append("serverstats."+ filename[:-3])
  if __name__ == '__main__':
    for extension in initial_extensions:
      client.load_extension(extension)
      
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cog_loader()
  
@client.event
async def on_ready():
  await client.change_presence(status=nextcord.Status.online ,activity=nextcord.Activity(type=nextcord.ActivityType.playing, name=f"Anime.exe"))
  cls()
  print('System online of {0.user}'.format(client))

#neverSleep.awake('https://mai-1.moazlion.repl.co/', False)
client.run(TOKEN)
