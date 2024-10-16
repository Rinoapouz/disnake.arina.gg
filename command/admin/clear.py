from extension.perms import HasAdministratorRole
import disnake
from disnake.ext import commands


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
            embed = disnake.Embed(
                title=f"You can't clear 0 Messages",
                color=disnake.Color.red()
            )
            await ctx.send(embed=embed)
        if message == 1:
            embed = disnake.Embed(
                title=f"{message} Message have been deleted",
                color=disnake.Color.red()
            )
            await ctx.send(embed=embed)

        if message > 2:
            embed = disnake.Embed(
                title=f"{message} Messages have been deleted",
                color=disnake.Color.red()
            )
            await ctx.send(embed=embed)

    @HasAdministratorRole()
    @bot.command(
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
    async def ariclear(ctx, message: int) -> None:
        await ctx.channel.purge(limit=message + 1)  # message + 1, um die Befehlsnachricht selbst einzuschließen
        if message == 0:
            embed = disnake.Embed(
                title=f"You can't clear 0 Messages",
                color=disnake.Color.red()
            )
            await ctx.send(embed=embed)
        if message == 1:
            embed = disnake.Embed(
                title=f"{message} Message have been deleted",
                color=disnake.Color.red()
            )
            await ctx.send(embed=embed)

        if message > 2:
            embed = disnake.Embed(
                title=f"{message} Messages have been deleted",
                color=disnake.Color.red()
            )
            await ctx.send(embed=embed)