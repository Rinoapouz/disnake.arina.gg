import time
import disnake
from disnake.ext import commands


def hilfe(bot):
    @bot.slash_command(
        name="help",
        description="Show all commands from the Bot Rinoa")
    async def slashhelp(ctx) -> None:
        embed = disnake.Embed(
            title="ᓚᘏᗢ",
            description="The Golden Cat can hear you with the prefix **ari or /**""",
            color=disnake.Color.yellow()
        )

        embed.add_field(
            name="🔗 Default",
            value="""```
/help
/level
                ```""",
            inline=True
        )

        embed.add_field(
            name="ℹ️ Information",
            value="""```
soon...
                ```""",
            inline=True
        )

        embed.add_field(
            name="🔧 Administrator",
            value="""```
/ban
/kick
/clear
/nuke
arisetup_verification
                ```""",
            inline=True
        )

        await ctx.send(embed=embed)