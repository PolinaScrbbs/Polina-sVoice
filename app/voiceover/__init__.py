import os
import random
import string
from edge_tts import Communicate

from ..config import MEDIA_FOLDER


async def to_voice(text: str, voice: str) -> str:
    communicate = Communicate(text, voice)

    os.makedirs(MEDIA_FOLDER, exist_ok=True)

    unique_suffix = "".join(random.choices(string.digits, k=4))
    filename = os.path.join(MEDIA_FOLDER, f"voice_{unique_suffix}.mp3")

    await communicate.save(filename)

    return filename
