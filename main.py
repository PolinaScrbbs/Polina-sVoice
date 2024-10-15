import asyncio
from edge_tts import Communicate

TEXT = "Родин пидорас"
OUTPUT_FILE = "russian.mp3"

async def amain() -> None:
    selected_voice = "ru-RU-DmitryNeural"
    communicate = Communicate(TEXT, selected_voice)
    await communicate.save(OUTPUT_FILE)
    print(f"Файл сохранён: {OUTPUT_FILE}")


if __name__ == "__main__":
    asyncio.run(amain())

