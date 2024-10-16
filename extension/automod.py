import disnake
from disnake.ext import commands
import settings

def automod(bot):
    @bot.event
    async def on_message(message):
        print(f"Received message: {message.content}")  # Log incoming messages

        if message.author == bot.user:
            return

        if any(word in message.content.lower() for word in settings.automod_bannedwords):
            await message.delete()
            await message.channel.send(f"{message.author.mention}, your message contained banned words and was deleted.")
    
        await bot.process_commands(message)