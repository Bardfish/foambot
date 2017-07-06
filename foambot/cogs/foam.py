from discord.ext import commands
from util.sampler import get_random_sample


class Foam:
    """Foam related commands"""

    def __init__(self, bot):
        self.bot = bot
        self.audio_player = bot.get_cog('AudioPlayer')

    @commands.command(pass_context=True)
    async def foam(self, ctx):
        await self.audio_player.play(ctx, get_random_sample(self.__class__.__name__, "we_got_foam"))

    @commands.command(pass_context=True)
    async def doctor(self, ctx):
        await self.audio_player.play(ctx, get_random_sample(self.__class__.__name__, "doctor"))

    @commands.command(pass_context=True)
    async def noises(self, ctx):
        await self.audio_player.play(ctx, get_random_sample(self.__class__.__name__, "noises"))

    @commands.command(pass_context=True)
    async def memes(self, ctx):
        await self.audio_player.play(ctx, get_random_sample(self.__class__.__name__, "custom"))

    @commands.command(pass_context=True)
    async def randum(self, ctx):
        await self.audio_player.play(ctx, get_random_sample(self.__class__.__name__, "/"))

    @commands.command(pass_context=True)
    async def halp(self, ctx):
        await self.bot.say(
            "Waddup mai foam friendly friends?! Here's a list of my commands. I only do voice commands at the moment"
            " but I plan to learn more things really soon :ok_hand:\n"
            "\nFoam COMMANDS:"
            "\n[--foam] Plays a sound related to foam and how much of it we has"
            "\n[--doctor] I'm a fucking doctor"
            "\n[--noises] Not very many, but they get the job done"
            "\n[--randum] An assortment of foam-related things without a specific category"
            "\n[--memes] Just for you my darlings"
        )

    async def on_message(self, message):
        if message.author.id != self.bot.user.id:
            contents = message.content.lower()
            if "--foam" not in contents and 'foam' in contents and 'foambot' not in contents:
                await self.bot.send_message(message.channel, 'Did someone say foam!? I gotz foam!!!!! :grimacing:')


def setup(bot):
    bot.add_cog(Foam(bot))
