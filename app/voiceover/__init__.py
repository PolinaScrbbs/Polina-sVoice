import os
import random
import string
from edge_tts import Communicate

from ..config import Config

async def to_voice(text: str) -> str:
    selected_voice = "ru-RU-DmitryNeural"
    communicate = Communicate(text, selected_voice)

    os.makedirs(Config.MEDIA_FOLDER, exist_ok=True)

    unique_suffix = ''.join(random.choices(string.digits, k=4))
    filename = os.path.join(Config.MEDIA_FOLDER, f'voice_{unique_suffix}.mp3')

    await communicate.save(filename)
    
    return filename