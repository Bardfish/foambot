import json
from discord.ext import commands
from audio import AudioPlayer


def load_credentials():
    with open('creds.json') as f:
        return json.load(f)


cmd_extensions = [
    'cogs.ping',
    'cogs.foam',
    'cogs.bizkit',
    'cogs.response'
]

description = "The ultimate annoy bot"
cmd_prefix = '--'
bot = commands.Bot(description=description, command_prefix=cmd_prefix)
bot.add_cog(AudioPlayer(bot))  # required for all audio-based cogs
for extension in cmd_extensions:
    bot.load_extension(extension)
creds = load_credentials()
bot.run(creds['token'])
