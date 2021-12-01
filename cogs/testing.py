import discord
import datetime
from cogs.utils import config
from discord.ext import commands
from setup_bot import StellaricBot


class Testing(commands.Cog, name="Testing"):
    """
    this is for test purposes
    """
  
    def __init__(self, bot: StellaricBot):
        self.bot = bot
    
    @commands.has_any_role(793679885285326890)
    @commands.command(message_command=False)
    async def only_slash(self, ctx: commands.Context):
        # This command can only be used with slash commands
        await ctx.send("Hello from slash commands!")

def setup(bot: StellaricBot):
  bot.add_cog(Testing(bot))