import time
import disnake
from disnake.ext import commands
import math
import random
import sqlite3

database = sqlite3.connect('arisu.sqlite')
cursor = database.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS levels(user_id INTERGER, guild_id INTEGER, exp INTEGER, level INTEGER, last_lvl INTEGER)""")


def leveling(bot):
    @bot.event
    async def on_message(ctx):
        if ctx.author.bot:
            return

        cursor.execute(f"SELECT user_id, guild_id, exp, level, last_lvl FROM levels WHERE user_id = {ctx.author.id} and guild_id = {ctx.guild.id}")
        results = cursor.fetchone()

        if results is None:

            cursor.execute(f"INSERT INTO levels(user_id, guild_id, exp, level, last_lvl) VALUES({ctx.author.id}, {ctx.guild.id}, 0, 0, 0)")
            database.commit()

        else:

            exp = results[2]
            lvl = results[3]
            last_lvl = results[4]

            exp_gained = random.randint(1, 20)
            exp += exp_gained
            lvl = 0.1 * (math.sqrt(exp))

            cursor.execute(f"UPDATE levels SET exp = {exp}, level = {lvl}, last_lvl = {last_lvl} WHERE user_id = {ctx.author.id} AND guild_id = {ctx.guild.id}")
            database.commit()

            if int(lvl) > last_lvl:

                await ctx.channel.send(f"{ctx.author.mention} has leveled up to {int(lvl)}!")
                cursor.execute(f"UPDATE levels SET last_lvl = {int(lvl)} WHERE user_id = {ctx.author.id} AND guild_id = {ctx.guild.id}")
                database.commit()