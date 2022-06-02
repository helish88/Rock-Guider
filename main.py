import disnake
from disnake.ext import commands


class RockGuider(commands.Bot):
    """Основной класс бота"""
    def __init__(self):
        super().__init__(
            intents=disnake.Intents(
                message_content=True,
                guilds=True
            ),
            test_guilds=[123456789]
        )


bot = RockGuider()


@bot.event
async def on_ready():
    bot.load_extension("cogs.guide")


if __name__ == "__main__":
    bot.run("token")
