import disnake
from disnake.ext import commands
import settings

def verifyreaction(bot):
    # Reaktion hinzufügen
    @bot.event
    async def on_raw_reaction_add(payload):
        if payload.channel_id == settings.verifysystem_VERIFY_CHANNEL_ID and str(payload.emoji) == settings.verifysystem_VERIFY_EMOJI:
            guild = bot.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            role = guild.get_role(settings.verifysystem_ROLE_ID)
            if role not in member.roles:
                await member.add_roles(role)

    # Reaktion entfernen
    @bot.event
    async def on_raw_reaction_remove(payload):
        if payload.channel_id == settings.verifysystem_VERIFY_CHANNEL_ID and str(payload.emoji) == settings.verifysystem_VERIFY_EMOJI:
            guild = bot.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            role = guild.get_role(settings.verifysystem_ROLE_ID)
            if role in member.roles:
                await member.remove_roles(role)