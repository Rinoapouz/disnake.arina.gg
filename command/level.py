import time
import disnake
from disnake.ext import commands
import sqlite3

# Connect to the SQLite3 database
database = sqlite3.connect('arisu.sqlite')
cursor = database.cursor()

# Function to create the level slash command
def level(bot):
    @bot.slash_command(
        name="level",
        description="Show your current level"
    )
    async def slashlevel(ctx):

        rank = 1

        # Query to get all users' levels in descending order of experience for the guild
        descending_query = """
        SELECT user_id, exp, level, last_lvl 
        FROM levels 
        WHERE guild_id = ? 
        ORDER BY exp DESC
        """
        cursor.execute(descending_query, (ctx.guild.id,))
        result = cursor.fetchall()

        # Determine the user's rank based on their position in the sorted results
        for i in range(len(result)):
            if result[i][0] == ctx.author.id:
                break
            else:
                rank += 1

        # Query to get the specific user's experience and level information
        user_query = """
        SELECT exp, level, last_lvl 
        FROM levels 
        WHERE user_id = ? AND guild_id = ?
        """
        cursor.execute(user_query, (ctx.author.id, ctx.guild.id))
        result = cursor.fetchone()

        if result:
            exp, level, last_lvl = result

            # Calculate the experience required for the next level
            next_lvl_xp = ((int(level) + 1) / 0.1) ** 2

            # Send the user's level and rank information
            await ctx.send(f"You're level: {int(level)} and your rank is: {rank}")
        else:
            await ctx.send("No level information found for you.")