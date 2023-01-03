import nextcord,os
from nextcord.ext import commands
from startup import cls
from config import TOKEN
from keep_alive import keep_alive

client = commands.Bot(
intents=nextcord.Intents.all(),
case_insensitive=True)

client.remove_command('help')
client.remove_command('purge')
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
  for filename in os.listdir("./commands/Naughty"):
    if filename.endswith(".py"):
      initial_extensions.append("commands.Naughty."+ filename[:-3])
  for filename in os.listdir("./commands/Utility"):
    if filename.endswith(".py"):
      initial_extensions.append("commands.Utility."+ filename[:-3])
        
  if __name__ == '__main__':
    for extension in initial_extensions:
      client.load_extension(extension)
      
cog_loader()

Nebula = """                                                               
888b    888 8888888888 888888b.         d8888 
8888b   888 888        888  "88b       d88888 
88888b  888 888        888  .88P      d88P888 
888Y88b 888 8888888    8888888K.     d88P 888 
888 Y88b888 888        888  "Y88b   d88P  888 
888  Y88888 888        888    888  d88P   888 
888   Y8888 888        888   d88P d8888888888 
888    Y888 8888888888 8888888P" d88P     888 
"""
@client.event
async def on_ready():
    cls()
    print(Nebula)
    await client.change_presence(activity=nextcord.Game(name="With monkeys"))

keep_alive()
client.run(TOKEN)
