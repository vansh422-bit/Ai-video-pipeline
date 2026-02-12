import asyncio
import edge_tts

async def text_to_speech(text, output_file="output/audio.mp3"):
    communicate = edge_tts.Communicate(text, "en-US-GuyNeural")
    await communicate.save(output_file)

def generate_voice(script):
    asyncio.run(text_to_speech(script))
