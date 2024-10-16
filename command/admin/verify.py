from extension.perms import HasAdministratorRole
import disnake
from disnake.ext import commands
import settings


def SetVerifyChannel(bot):
    @HasAdministratorRole()
    @bot.command()
    async def verifychannel(ctx):
        if ctx.channel.id == settings.verifysystem_VERIFY_CHANNEL_ID:
            embed = disnake.Embed(
                title="Verification",
                description="Click on the ✅ to verify yourself and gain access to the ✩ RinoaGang server.",
                color=disnake.Color.green()
            )
            msg = await ctx.send(embed=embed)
            await msg.add_reaction(settings.verifysystem_VERIFY_EMOJI)