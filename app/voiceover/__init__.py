import os
from edge_tts import Communicate

from ..config import Config

async def to_voice(text: str) -> str:
    selected_voice = "ru-RU-DmitryNeural"
    communicate = Communicate(text, selected_voice)
    
    os.makedirs(Config.MEDIA_FOLDER, exist_ok=True)
    filename = os.path.join(Config.MEDIA_FOLDER, 'voice_output.mp3')
    
    await communicate.save(filename)
    
    return filename