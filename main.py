import neverSleep
import nextcord
from nextcord.ext import commands,tasks
from itertools import cycle
import os
from startup import cls
from keep_alive import keep_alive

client = commands.Bot(command_prefix = "m!" , intents=nextcord.Intents.all(),case_insensitive=True)       
client.remove_command('help')
client.remove_command("purge")
initial_extensions = []

def cog_loader():
  for filename in os.listdir("./events/message"):
    if filename.endswith(".py"):
      initial_extensions.append("events.message."+ filename[:-3])
  for filename in os.listdir("./events/member"):
    if filename.endswith(".py"):
      initial_extensions.append("events.member."+ filename[:-3])
  
  for filename in os.listdir("./commands/Fun"):
    if filename.endswith(".py"):
      initial_extensions.append("commands.Fun."+ filename[:-3])
  for filename in os.listdir("./commands/Links"):
    if filename.endswith(".py"):
      initial_extensions.append("commands.Links."+ filename[:-3])
  for filename in os.listdir("./commands/Naughty"):
    if filename.endswith(".py"):
      initial_extensions.append("commands.Naughty."+ filename[:-3])
  for filename in os.listdir("./commands/Phrases"):
    if filename.endswith(".py"):
      initial_extensions.append("commands.Phrases."+ filename[:-3])
  for filename in os.listdir("./commands/Utility"):
    if filename.endswith(".py"):
      initial_extensions.append("commands.Utility."+ filename[:-3])
        
  if __name__ == '__main__':
    for extension in initial_extensions:
      client.load_extension(extension)
      
cog_loader()

status = cycle([
    'Anime.exe',
    '!help',
    'With you',
    'Rocket League',
    'Genshin Impact',
    'Elden Ring',
    'Apex Legemds',
    'Anime',
    'Chess',
    'Rape Session',
    'Hanime',
    'Touching Grass',
    'Waius Pouts'
])

@tasks.loop(seconds=1800)
async def status_swap():
    await client.change_presence(activity=nextcord.Game(next(status)))

@client.event
async def on_ready():
    cls()
    print('{0.user} is now online'.format(client))
    status_swap.start()

neverSleep.awake('https://Hayasaka.moazlion.repl.co/', False)
keep_alive()
client.run(os.getenv('TOKEN'))
