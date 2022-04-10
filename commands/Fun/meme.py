import nextcord
from nextcord.ext import commands
import random
import datetime
import asyncpraw
from config import green

class Meme(commands.Cog):
    def __init__(self, client):
         self.client = client
      
    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def meme(self, ctx, subred="memes"):
        msg = await ctx.send('Loading ... This will take time depending on your internet')

        reddit = asyncpraw.Reddit(client_id='csQxQNU-rrSIOPecjqL8Jw',
        client_secret='p7GQRyGHyrco8HNA-oS4jODwL5EoMw',
        username='Moazlion',
        password='mo757677',
        user_agent='praw123')

        subreddit = await reddit.subreddit("memes")
        all_subs = []
        top = subreddit.top(limit=250) 

        async for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        eme = nextcord.Embed(title=f'__{name}__', colour=green)
        eme.timestamp = datetime.datetime.utcnow()
        eme.set_image(url=url)
        eme.set_footer(text='Here is your meme!')
        await ctx.send(embed=eme)
        await msg.edit(content=f'<https://reddit.com/r/{subreddit}/> :smirk:') 
        return

    @meme.error
    async def meme_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        em = nextcord.Embed(title=f"Woah Slow it down buckaroo!",description=f"Try again in **{error.retry_after:.2f}s**", color=0xe74c3c)
        await ctx.send(embed=em)
      else:
        emb = nextcord.Embed(title=f"Something went wrong!",description=f"Tell Moaz about this error if possible", color=0xe74c3c)
        await ctx.send(embed=emb)
    
def setup(client):
    client.add_cog(Meme(client))
    