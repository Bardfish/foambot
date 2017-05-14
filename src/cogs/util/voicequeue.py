from discord import ClientException


class VoiceQueue:
    def __init__(self, bot):
        self.bot = bot
        self.playing = False
        self.playlist = []
        self.vc = None
        self.voice = None

    async def join_voice_channel(self, vc):
        self.voice = await self.bot.join_voice_channel(vc)
        self.vc = vc

    async def add(self, file_name, vc, tc, server):
        if not self.bot.is_voice_connected(server):
            try:
                await self.join_voice_channel(vc)
            except ClientException:
                # TODO create the correct solution for handling this
                # for some reason that function will say it's disconnected even if it is connected
                await self.voice.disconnect()
                await self.join_voice_channel(vc)
        else:
            if vc != self.vc:
                if self.playing:
                    await self.bot.send_message(tc, "I'm playing with my other buddies right now. Try again when I'm"
                                                    " not busy")
                    return
                else:
                    await self.voice.disconnect()
                    await self.join_voice_channel(vc)

        self.playlist.append(file_name)
        if not self.playing:
            self.playing = True
            self.play()

    def play(self):
        player = self.voice.create_ffmpeg_player(self.playlist.pop(0),
                                                 after=self._play_helper)
        player.start()

    def _play_helper(self):
        """ This method only gets called after a song has finished playing.
            This is the only safe time to set the players status to False
        """
        if len(self.playlist) == 0:
            self.playing = False
        else:
            self.play()  # continue the recursive evaluation of our queued voice clips
