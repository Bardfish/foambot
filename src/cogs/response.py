from discord.ext import commands

class Response:
    """Responding to being mentioned"""

    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        if message.author.id != self.bot.user.id:
            contents = message.content.lower()
            if "thanks foambot" in contents or "thank you foambot" in contents:
                await self.bot.send_message(message.channel, "You're very welcome, my foamy friend!!! ^-^")
            elif "foambot" in contents:
                await self.bot.send_message(message.channel, "Did someone say foambot?? Dat's my name! I'm foambot, and I'm here to help!! WeEee~~~ :grimacing:")

def setup(bot):
    bot.add_cog(Response(bot))
