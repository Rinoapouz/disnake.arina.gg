import disnake
from disnake.ext import commands
from botsettings import COUNTING_CHANNEL_ID


current_count = 1
last_user_id = None

def counting(bot):
    @bot.event
    async def on_message(message):
        global current_count, last_user_id
    
        # Ignoriere Bot-Nachrichten und Nachrichten aus anderen Kanälen
        if message.author.bot or message.channel.id != COUNTING_CHANNEL_ID:
            return

        # Prüfe, ob die Nachricht eine Zahl enthält und gleich der erwarteten Zahl ist
        try:
            user_count = int(message.content)
        except ValueError:
            return  # Ignoriere Nachrichten, die keine Zahl enthalten

        # Prüfen, ob der Nutzer versucht, zwei Zahlen nacheinander zu senden
        if message.author.id == last_user_id:
            await message.channel.send(
                f"{message.author.mention}, You can't count twice in a row! Restart at **1**!"
            )
            current_count = 1  # Reset auf 1
            last_user_id = None  # Letzten Nutzer zurücksetzen
            return

        # Prüfen, ob die Zahl korrekt ist
        if user_count == current_count:
            # Wenn korrekt, erhöhe den Zähler und speichere die User-ID
            current_count += 1
            last_user_id = message.author.id
        else:
            # Wenn die Zahl falsch ist, setze den Zähler zurück
            await message.channel.send(
                f"Oops! {message.author.mention} posted the wrong number. Restart at **1**!"
            )
            current_count = 1  # Reset auf 1
            last_user_id = None  # Letzten Nutzer zurücksetzen