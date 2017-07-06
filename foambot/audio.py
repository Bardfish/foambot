import asyncio
from discord.ext import commands


class VoiceEntry(object):
    def __init__(self, message, player):
        self.requester = message.author
        self.channel = message.channel
        self.player = player


class VoiceState(object):
    def __init__(self, bot):
        self.current = None
        self.voice = None
        self.bot = bot
        self.play_next_song = asyncio.Event()
        self.clips = asyncio.Queue()
        self.audio_player = self.bot.loop.create_task(self.audio_player_task())

    @property
    def player(self):
        return self.current.player

    def is_playing(self):
        if self.voice is None or self.current is None:
            return False
        return not self.player.is_done()

    async def audio_player_task(self):
        while True:
            self.play_next_song.clear()
            self.current = await self.clips.get()
            self.player.start()
            await self.play_next_song.wait()

    def toggle_next(self):
        self.bot.loop.call_soon_threadsafe(self.play_next_song.set)


class AudioPlayer(object):
    def __init__(self, bot):
        self.bot = bot
        self.voice_states = {}

    def get_voice_state(self, server):
        state = self.voice_states.get(server.id)
        if state is None:
            state = VoiceState(self.bot)
            self.voice_states[server.id] = state
        return state

    async def create_voice_client(self, channel):
        voice = await self.bot.join_voice_channel(channel)
        state = self.get_voice_state(channel.server)
        state.voice = voice

    def __unload(self):
        for state in self.voice_states.values():
            try:
                state.audio_player.cancel()
                if state.voice:
                    self.bot.loop.create_task(state.voice.disconnect())
            except:
                pass

    @commands.command(pass_context=True, no_pm=True)
    async def summon(self, ctx):
        summoned_channel = ctx.message.author.voice_channel
        if summoned_channel is None:
            await self.bot.say('You aren\'t in a voice channel M\'Lord')
            return False
        state = self.get_voice_state(ctx.message.server)
        if state.voice is None:
            state.voice = await self.bot.join_voice_channel(summoned_channel)
        else:
            await state.voice.move_to(summoned_channel)

        return True

    async def play(self, ctx, file_name):
        state = self.get_voice_state(ctx.message.server)
        if state.voice is None:
            success = await ctx.invoke(self.summon)
            if not success:
                return

        try:
            player = state.voice.create_ffmpeg_player(file_name, after=state.toggle_next)
        except Exception as e:
            fmt = 'An error occurred while processing this request: ```py\n{}: {}\n```'
            await self.bot.send_message(ctx.message.channel, fmt.format((type(e)), e))

        else:
            player.volume = 0.6
            entry = VoiceEntry(ctx.message, player)
            await state.clips.put(entry)
