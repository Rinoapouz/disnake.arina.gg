from extension.permissions import HasAdministratorRole
import disnake
from disnake.ext import commands
from botsettings import embed_VERIFY, verifysystem_VERIFY_CHANNEL_ID, verifysystem_VERIFY_EMOJI


def SetVerifyChannel(bot):
    @HasAdministratorRole()
    @bot.command()
    async def verifychannel(ctx):
        if ctx.channel.id == verifysystem_VERIFY_CHANNEL_ID:
            msg = await ctx.send(embed=embed_VERIFY)
            await msg.add_reaction(verifysystem_VERIFY_EMOJI)