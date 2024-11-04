from extension.permissions import HasAdministratorRole
import disnake
from disnake.ext import commands
from botsettings import embed_CLEAR0, embed_CLEAR1

def clear(bot):
    @HasAdministratorRole()
    @bot.slash_command(
        name="clear",
        description="Clear a sort of content",
        options=[
            disnake.Option(
                name="message",
                description="How much you want to clear",
                type=disnake.OptionType.integer,
                required=True
            ),
        ]
    )
    async def slashclear(ctx, message: int) -> None:
        await ctx.channel.purge(limit=message + 1)  # message + 1, um die Befehlsnachricht selbst einzuschließen
        if message == 0:
            await ctx.send(embed=embed_CLEAR0, ephemeral=True)
        if message == 1:
            await ctx.send(embed=embed_CLEAR1, ephemeral=True)
        if message > 2:
            await ctx.send(embed=embed_CLEAR1, ephemeral=True)