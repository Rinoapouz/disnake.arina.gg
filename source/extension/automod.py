import disnake
from disnake.ext import commands
from botsettings import automod_BANNEDWORDS

def automod(bot):
    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        if any(word in message.content.lower() for word in automod_BANNEDWORDS):
            await message.delete()
