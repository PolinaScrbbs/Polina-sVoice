import edge_tts


async def get_voices_name():
    voices = await edge_tts.list_voices()
    voice_names = sorted(set(voice["Name"] for voice in voices))
    return voice_names
