
import discord
from discord.ext import commands

import json

class ServerOwner(commands.Cog):
    """Commands for server owners """
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def setprefix(self, ctx, *, pre):
        with open(r"/root/bots/Guren/cogs/prefixes.json", "r") as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = pre
        await ctx.send(f"New guild prefix is `{pre}`")

        with open(r"/root/bots/Guren/cogs/prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)

def setup(bot):
    bot.add_cog(ServerOwner(bot))
