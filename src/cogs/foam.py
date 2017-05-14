import random
import os
from discord.ext import commands

SAMPLES_DIR = os.path.abspath("./../samples")


class Foam:
    """Foam related commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def foam(self, ctx):
        vc = ctx.message.author.voice_channel
        tc = ctx.message.channel
        if vc:
            await self.bot.player.add(
                os.path.abspath(
                    SAMPLES_DIR + "/we_got_foam/" + random.choice(os.listdir(SAMPLES_DIR + "/we_got_foam"))), vc, tc)
        else:
            await self.bot.send_message(tc, "You're not in any voice channels mai foam friendly friend!")

    @commands.command(pass_context=True)
    async def doctor(self, ctx):
        vc = ctx.message.author.voice_channel
        tc = ctx.message.channel
        if vc:
            await self.bot.player.add(
                os.path.abspath(
                    SAMPLES_DIR + "/doctor/" + random.choice(os.listdir(SAMPLES_DIR + "/doctor"))), vc, tc)
        else:
            await self.bot.send_message(tc, "You're not in any voice channels mai foam friendly friend!")

    @commands.command(pass_context=True)
    async def noises(self, ctx):
        vc = ctx.message.author.voice_channel
        tc = ctx.message.channel
        if vc:
            await self.bot.player.add(
                os.path.abspath(
                    SAMPLES_DIR + "/noises/" + random.choice(os.listdir(SAMPLES_DIR + "/noises"))), vc, tc)
        else:
            await self.bot.send_message(tc, "You're not in any voice channels mai foam friendly friend!")

    @commands.command(pass_context=True)
    async def memes(self, ctx):
        vc = ctx.message.author.voice_channel
        tc = ctx.message.channel
        if vc:
            await self.bot.player.add(
                os.path.abspath(
                    SAMPLES_DIR + "/custom/" + random.choice(os.listdir(SAMPLES_DIR + "/custom"))), vc, tc)
        else:
            await self.bot.send_message(tc, "You're not in any voice channels mai foam friendly friend!")

    @commands.command(pass_context=True)
    async def random(self, ctx):
        vc = ctx.message.author.voice_channel
        tc = ctx.message.channel
        if vc:
            await self.bot.player.add(
                os.path.abspath(
                    SAMPLES_DIR + "/" + random.choice(os.listdir(SAMPLES_DIR))), vc, tc)
        else:
            await self.bot.send_message(tc, "You're not in any voice channels mai foam friendly friend!")

    @commands.command(pass_context=True)
    async def halp(self, ctx):
        await self.bot.say(
            "Waddup mai foam friendly friends?! Here's a list of my commands. I only do voice commands at the moment"
            " but I plan to learn more things really soon :aaam:\n"
            "\nCOMMANDS:"
            "\n[--foam] (plays a sound related to foam and how much of it we have)"
            "\n[--doctor] (I'm a fucking doctor)"
            "\n[--noises] (Not very many, but they get the job done)"
            "\n[--random] (An assortment of foam-related things without a specific category)"
            "\n[--memes] (Just for you my darlings)")

    async def on_message(self, message):
        if message.author.id != self.bot.user.id:
            contents = message.content.lower()
            if "--foam" not in contents and 'foam' in contents:
                await self.bot.send_message(message.channel, 'Did someone say foam!? I gotz foam!!!!! :grimacing:')


def setup(bot):
    bot.add_cog(Foam(bot))
