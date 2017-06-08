import json
from discord.ext import commands
from cogs.util.voicequeue import VoiceQueue


def load_credentials():
    with open('creds.json') as f:
        return json.load(f)

cmd_extensions = [
    'cogs.ping',
    'cogs.foam',
    'cogs.response'
]

description = "The ultimate annoy bot"
cmd_prefix = '--'
bot = commands.Bot(description=description, command_prefix=cmd_prefix)
bot.player = VoiceQueue(bot)
for extension in cmd_extensions:
    bot.load_extension(extension)
creds = load_credentials()
bot.run(creds['token'])
