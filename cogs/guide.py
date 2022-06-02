from typing import List
import json

import disnake
from disnake.ext import commands


def get_keys(path: str) -> List[str]:
    """Возвращает список внешних ключей из json файла"""
    with open(path, 'r', encoding='utf-8') as file:
        return [key for key in json.loads(file.read())]


bioms = commands.option_enum(get_keys('guide/bioms.json'))
mobs = commands.option_enum(get_keys('guide/mobs.json'))


class Guide(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.emojies = {
            ":features:": self.bot.get_emoji(980808043065397248),
            ":health:": self.bot.get_emoji(980792262646702090),
            ":damage:": self.bot.get_emoji(980808043010867250),
            ":croppa:": self.bot.get_emoji(981199236651708416),
            ":umanite:": self.bot.get_emoji(981199736512086086),
            ":jadiz:": self.bot.get_emoji(981200051265212468),
            ":bismor:": self.bot.get_emoji(981200577109327933),
            ":magnite:": self.bot.get_emoji(981200851630694420),
            ":enor:": self.bot.get_emoji(981201224906993705)
        }

    def get_embed(self, theme: str, name: str) -> disnake.Embed:
        """Возвращает Embed из json файла в директории guide"""
        with open(f"guide\\{theme}.json", 'r', encoding='utf-8') as file:
            data = json.loads(file.read())[name]

        # переделываем :эмодзи: для дискорда
        for field in data['fields']:
            for k, v in self.emojies.items():
                field["name"] = field['name'].replace(k, str(v))
                field["value"] = field['value'].replace(k, str(v))

        return disnake.Embed.from_dict(data)

    # Биом
    @commands.slash_command(name="биом")
    async def biome(
        self,
        inter: disnake.ApplicationCommandInteraction,
        name: bioms
    ):
        await inter.send(embed=self.get_embed('bioms', name))

    # Существо
    @commands.slash_command(name='существо')
    async def mob(
        self,
        inter: disnake.ApplicationCommandInteraction,
        name: mobs
    ):
        await inter.send(embed=self.get_embed('mobs', name))


def setup(bot: commands.Bot):
    bot.add_cog(Guide(bot))
