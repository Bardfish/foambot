from discord.ext import commands
from util.sampler import get_random_sample


class Bizkit:
    """All commands Limp Bizkit related"""

    def __init__(self, bot):
        self.bot = bot
        self.audio_player = bot.get_cog('AudioPlayer')

    @commands.command(pass_context=True)
    async def goldcobra(self, ctx):
        await self.audio_player.play(ctx, get_random_sample(self.__class__.__name__, "gcobra"))

    @commands.command(pass_context=True)
    async def fred(self, ctx):
        await self.audio_player.play(ctx, get_random_sample(self.__class__.__name__, "/"))

    @commands.command(pass_context=True)
    async def rollin(self, ctx):
        await self.audio_player.play(ctx, get_random_sample(self.__class__.__name__, "rollin"))

    @commands.command(pass_context=True)
    async def yeah(self, ctx):
        await self.audio_player.play(ctx, get_random_sample(self.__class__.__name__, "yeah"))

    @commands.command(pass_context=True)
    async def dursthelp(self, ctx):
        await self.bot.say(
            "Yeah! Fuck all y'all haters let's do it Gold Cobra Style!\n"
            "\nBizkit COMMANDS:"
            "\n[--goldcobra] It's so gold y'all"
            "\n[--fred] That's me"
            "\n[--rollin] rollin rollin rollin"
            "\n[--yeah] YEAH!"
        )


def setup(bot):
    bot.add_cog(Bizkit(bot))
