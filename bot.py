import disnake
from disnake.ext import commands

# lädt die anderen commands und extension
#
from command.help import * 
from command.level import *
from command.admin.clear import *
from command.admin.nuke import *
from command.admin.verify import *
# 
from extension.levelsystem import *
from extension.automod import *
from extension.verifysystem import *

# Kombiniert alle Commands / Extension und packt die in eine Liste
command = [clear, nuke, help, level, SetVerifyChannel]
extension = [verifyreaction, leveling, automod]



# bots intents
intents = disnake.Intents.all()
bot = commands.Bot(
    command_prefix="ari",  # Bot Prefix (worauf der Bot hört)
    intents=intents,  # Pass the intents
    help_command=None,  # Entferne das ugly help
    activity=disnake.Game(name="nothing")  # Bot Status setzen
)

@bot.event      
async def on_ready():
    print(f"The Bot is working")

# Lädt die liste und aktiviert die Commands
for command in command:
    command(bot)
for extension in extension:
    extension(bot)

# Lädt den Bot Token und startet ihn
bot.run("")