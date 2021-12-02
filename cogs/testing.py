import discord
import datetime
from cogs.utils import checks, config
from discord.ext import commands
from discord.utils import get
from setup_bot import StellaricBot

class Testing(commands.Cog, name="Testing", hidden=True):
  
    def __init__(self, bot: StellaricBot):
        self.bot = bot
    
    @commands.has_any_role(793679885285326890)
    @commands.command()
    async def deleteslash(self, ctx, gid: int):
        if author.id == 341837496763678731:
            await self.bot.http.bulk_upsert_guild_commands(self.bot.application_id, gid, [])
            return
        else:
            return


def setup(bot: StellaricBot):
  bot.add_cog(Testing(bot))