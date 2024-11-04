import time
import disnake
from disnake.ext import commands
from botsettings import BOTNAME, embed_HELP

def help(bot):
    @bot.slash_command(
        name="help",
        description="Show all commands from the Bot Arina.gg"
        )
    async def slashhelp(ctx) -> None:
        await ctx.send(embed=embed_HELP, ephemeral=True)
