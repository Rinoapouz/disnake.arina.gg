import time
import disnake
from disnake.ext import commands

# Overall Settings
BOTNAME = "Arina.gg"



#Verifysystem
verifysystem_ROLE_ID = 1288444542445424703
verifysystem_VERIFY_CHANNEL_ID = 1283331136789024792
verifysystem_VERIFY_EMOJI = "✅" # :white_check_mark:

#Levelsystem
levelsystem_LEADERBOARD_CHANNEL_ID = 1295678878471163998

#Automod
automod_BANNEDWORDS = ['badword1', 'badword2', 'anotherbadword']

#Permissions
permissions_ADMINISTRATOR = ["Founder", "Administrator", "Helper"]


#
#
##Games

#Games_Counting
COUNTING_CHANNEL_ID = 1295370202841878568



#
#
##Embeds
normal_embed_color= 0x397882
admin_embed_color= 0xf70502

#Embeds_Level





#Embeds_help
embed_HELP = disnake.Embed(
    title="ᓚᘏᗢ",
    description="Arina.gg can hear you with the prefix  **/**",
    color=normal_embed_color
)
embed_HELP.add_field(name="🔗 Default", value="```/help \n/level ```", inline=True)
embed_HELP.add_field(name="ℹ️ Information", value="```The bot is still in Development```", inline=True)
embed_HELP.add_field(name="🔧 Administrator", value="```/clear \n/nuke \narisetup_verification ```", inline=True)

#Embeds_Verify
embed_VERIFY = disnake.Embed(
    title="Verification",
    description="Click on the ✅ to verify yourself and gain access to the **✩ RinoaGang** server.",
    color=admin_embed_color
)

#Embeds_Nuke
embed_NUKE = disnake.Embed(
    title=f"The channel has been nuked.",
    color=admin_embed_color
)

#Embeds_Clear
embed_CLEAR0 = disnake.Embed(
    title=f"You can't clear 0 Messages",
    color=admin_embed_color
)
embed_CLEAR1 = disnake.Embed(
    title=f"Messages have been deleted",
    color=admin_embed_color
)



