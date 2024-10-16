import edge_tts

async def get_available_voices():
    voices = await edge_tts.list_voices()
    
    unique_languages = set()
    unique_voices = set()
    
    for voice in voices:
        unique_languages.add(voice['Locale'])
        unique_voices.add(voice['Name'])
    
    print("Уникальные языки:")
    for language in unique_languages:
        print(language)
    
    print("\nУникальные озвучки:")
    for voice in unique_voices:
        print(voice)