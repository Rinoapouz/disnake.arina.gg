import disnake
from disnake.ext import commands
import sqlite3
from datetime import datetime

# Connect to the SQLite3 database
database = sqlite3.connect('arina.sqlite')
cursor = database.cursor()

# Function to create the level slash command
def level(bot):
    @bot.slash_command(
        name="level",
        description="Show your current level"
    )
    async def slashlevel(inter):  # Changed 'ctx' to 'inter' for interactions

        rank = 1

        # Query to get all users' levels in descending order of experience for the guild
        descending_query = """
        SELECT user_id, exp, level, last_lvl 
        FROM levels 
        WHERE guild_id = ? 
        ORDER BY exp DESC
        """
        cursor.execute(descending_query, (inter.guild.id,))
        result = cursor.fetchall()

        # Determine the user's rank based on their position in the sorted results
        for i in range(len(result)):
            if result[i][0] == inter.author.id:
                break
            else:
                rank += 1

        # Query to get the specific user's experience and level information
        user_query = """
        SELECT exp, level, last_lvl 
        FROM levels 
        WHERE user_id = ? AND guild_id = ?
        """
        cursor.execute(user_query, (inter.author.id, inter.guild.id))
        result = cursor.fetchone()

        if result:
            exp, level, last_lvl = result

            # Calculate the experience required for the next level
            next_lvl_xp = ((int(level) + 1) / 0.1) ** 2

            # Calculate progress bar boxes
            total_xp_for_level = 200 * (0.5 * int(level))
            boxes = int((exp / total_xp_for_level) * 20)

            # Send the user's level and rank information
            embed = disnake.Embed(
                title=f"{inter.author.name}'s Level Stats",
                description="",
                color=0x397882
            )
            embed.add_field(name="Name", value=inter.author.mention, inline=True)
            embed.add_field(name="Level", value=str(level), inline=True)
            embed.add_field(name="Rank", value=f"{rank}/{inter.guild.member_count}", inline=True)
            embed.add_field(
                name="Progress Bar",
                value=boxes * "🟦" + (20 - boxes) * "⬜",
                inline=False
            )
            embed.set_thumbnail(url=inter.author.display_avatar)

            # Send as an ephemeral message (only visible to the user)
            await inter.send(embed=embed, ephemeral=True)
        else:
            await inter.send("No level information found for you.", ephemeral=True)
