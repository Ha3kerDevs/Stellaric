import discord, time
import datetime
from discord.ext import commands
from cogs.utils import config
from typing import Optional
from cogs.utils import utils as StellaricUtils
from cogs.utils import checks
from discord.utils import get
from setup_bot import StellaricBot

# 793679885285326890 = Developer (Own Server)
# 797687618007466015 = Moderator (Own Server)
# 822428355554312212 = Founder
# 823814683973779488 = Co-Founder
# 822727647087165461 = Head Admin
# 823048526610038796 = Admin
# 825584517963055174 = Manager
# 823048690058526730 = Head Moderator
# 823048862821777438 = Senior Moderator
# 823372056409800724 = Moderator
# 826833464401330177 = Helper


# <a:utility:831769452344639498>\u2800
class Utility(commands.Cog, name="Utility"):
  """
  Utility commands idk :p
  """
  
  def __init__(self, bot: StellaricBot):
    self.bot = bot

  @commands.has_any_role(
    793679885285326890,
    797687618007466015,
    822428355554312212,
    823814683973779488,
    822727647087165461
  )
  @commands.cooldown(1, 6, commands.BucketType.guild)
  @commands.guild_only()
  @commands.command(help="Nukes (Mass purge) a channel. For staff only.")
  async def nuke(self, ctx):
    exe_start = time.time()
    pos = ctx.channel.position
    await ctx.channel.delete(reason=f"{ctx.channel.name} has been nuked")
    channel = await ctx.channel.clone()
    await channel.edit(position=pos)
    await channel.send(f"Nuke successful. [Execution time: {time.time() - exe_start}]", delete_after=11)

  #@commands.has_any_role()
  @commands.cooldown(1, 6, commands.BucketType.user)
  @commands.guild_only()
  @commands.command(
    name="membercount",
    help="check how many members in Stellaric.",
    aliases=["mc"]
  )
  async def _membercount(self, ctx):
    member_count = len(ctx.guild.members)
    true_member_count = len([m for m in ctx.guild.members if not m.bot])

    embed = discord.Embed(title="Member Count", description=
      f"Total: {member_count}\n"
      f"True Count: {true_member_count}",
      color=0xf8c7c7
    )
    await ctx.reply(embed=embed, allowed_mentions=discord.AllowedMentions().none())
  
  @commands.has_any_role(
    793679885285326890,
    797687618007466015,
    822428355554312212,
    823814683973779488,
    822727647087165461
  )
  @commands.guild_only()
  @commands.command(
    name='timedif',
    help='For staff only.',
    usage='<id1> <id2>',
    aliases=['td']
  )
  async def timedif(
      self, ctx, 
      id1: Optional[str] = commands.Option(description="PLEASE PRESS TAB WHEN YOU FINISHED PASTING ID1"), 
      id2: Optional[str] = commands.Option(description="PLEASE PRESS TAB WHEN YOU FINISHED PASTING ID2")
    ):
      try:
        id1 = int(id1)
        id2 = int(id2)
          
      except:
          await ctx.send("Check your message ID's! They are incorrect!")
          
      time1 = discord.utils.snowflake_time(int(id1))
      time2 = discord.utils.snowflake_time(int(id2))
      
      ts_diff = time2 - time1
      secs = abs(ts_diff.total_seconds())
      answer='{} secs'.format(secs)
      
      embed = discord.Embed(title="Time Difference", description=f"Time: {answer}", color=0xf8c7c7)
      await ctx.send(embed=embed)

  @commands.has_any_role(
    793679885285326890,
    797687618007466015,
    822428355554312212,
    823814683973779488,
    822727647087165461,
    823048526610038796,
    825584517963055174,
    823048690058526730,
    823048862821777438,
    823372056409800724,
    826833464401330177
  )
  @commands.cooldown(1, 3, commands.BucketType.user)
  @commands.command(pass_context=True,
    name="winlog",
    help='logs the winner of a giveaway.',
    usage='<user>, <giveaway type> and <item>',
  )
  async def _winlog(self, ctx, user: discord.Member, gtype, *, item):
    channel = user.guild.get_channel(831133427159400468)
    text = arg.upper()
    #thenlog = discord.Embed(
    #  title=f"Win log",
    #  description=f"**Got Logged:** {str(user)} [`{user.id}`]\n"
    #  f"**Giveaway Type | Item:** `{gtype}` | `{text}`\n"
    #  f"**Responsible:** {ctx.author.mention}",
    #  color=0xf8c7c7
    #)
    #auditlog.set_thumbnail(url=user.avatar_url)
    #thenlog.set_footer(text=f"Stellaric Logs | Author ID: {ctx.author.id}")

    await ctx.send(f"[ {user.mention} ] Claimed **{item}** from {gtype}")

    await ctx.message.delete()
  
  @commands.has_any_role(
    793679885285326890,
    797687618007466015,
    822428355554312212,
    823814683973779488,
    822727647087165461
  )
  @commands.guild_only()
  @commands.command(
    name="noreq",
    help="Testing."
  )
  async def _noreq(self, ctx):
    
    line = "<:sl_blueline:915258046660354078>"
    dot2 = "<:s_dots:915257866468868146>"
    horn = "<:s_horn:915257645848473650>"
    gift = "<:s_gift:915257902145617981>"

    finalline = f"{dot2} {line}{line}{line}{line}{line}{line}{line}{line}{line}{line}{line}{line}{line}{line}{line}{line} {dot2}"
    await ctx.send(
    f"╭ {gift} **NO REQUIREMENTS, ENJOY!**\n"
    f"{finalline}\n "
    f"\u2800{horn} **TIPS:**\n"
    f"\u2800{dot2} Putting **Stellaric** at the topn of your server list will help you see our pings easily!\n"
    f"\u2800{dot2} Make sure to **prioritize our pings** so you won't miss any giveaways!\n"
    f"\u2800{dot2} Be active in Stellaric for more!\n"
    f"{finalline}\n"
    f"╰ {gift} **Stay in Stellaric for more giveaways like this!**"
    )
    await ctx.message.delete()



def setup(bot: StellaricBot):
  bot.add_cog(Utility(bot))