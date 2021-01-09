import asyncio

import discord
from discord.ext import commands
from . import config


class Administration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="kick", help="kicks a member from the guild if you have the right")
    async def kick_member(self, ctx, member: discord.Member):
        if ctx.author.top_role < member.top_role:
            await ctx.send("Cannot kick member ! you don't have the right !")
        else:
            await ctx.guild.kick(member)


class Communication(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['announce', 'ann', 'send_announcement', 'important', 'annonce'], name="announcement",
                      help="Copies the message into announcement channel and mentions everyone, deltes the sent message")
    async def send_announcement(self, ctx, *, message):
        roles = ctx.guild.roles
        student_role = None
        msg = None
        for role in roles:
            if role.name.lower() == "student":
                student_role = role
        if ctx.author.top_role <= student_role:
            msg = await ctx.send("You don't have permission to send announcements")
        else:
            channel = None
            for c in ctx.guild.channels:
                if c.name.lower() == config.announcement_channel:
                    channel = c
                    break
            if channel is not None:
                await channel.send("{0} ".format(student_role.mention) + message)
        await ctx.message.delete()
        await asyncio.sleep(4)
        if msg is not None:
            await msg.delete()


class Editing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="nickname", help="changes someone else's nickname, leave it empty for removing nickname")
    async def change_nickname(self, ctx, user: discord.Member, *, username=""):
        if user is None:
            await ctx.send("member {0} not found!".format(user))
        if user.top_role > ctx.author.top_role:
            await ctx.send("You can't change {0} nickname".format(user.display_name))
        else:
            try:
                await user.edit(nick=username)
            except discord.Forbidden:
                await ctx.send("user is higher than me, do it manually")


def set_commands(bot: commands.Bot):
    bot.add_cog(Editing(bot))
    bot.add_cog(Administration(bot))
    bot.add_cog(Communication(bot))
