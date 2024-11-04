import time
from extension.permissions import HasAdministratorRole
import disnake
from disnake.ext import commands
from botsettings import embed_NUKE

def nuke(bot):
    @HasAdministratorRole()
    @bot.slash_command(
        name="nuke",
        description="Clear the channel")
    async def slashnuke(ctx) -> None:
        await ctx.channel.purge()
        await ctx.send(embed=embed_NUKE, ephemeral=True)