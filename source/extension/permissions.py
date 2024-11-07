import time
import disnake
from disnake.ext import commands
from botsettings import permissions_ADMINISTRATOR


# Checkt ob der User die Rollen hat für den Befehl 
def HasAdministratorRole():
    async def predicate(ctx):
        return any(
            role.name in permissions_ADMINISTRATOR for role in ctx.author.roles) or ctx.author.guild_permissions.administrator
    return commands.check(predicate)