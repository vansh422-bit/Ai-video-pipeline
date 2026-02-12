from script_generator import generate_script
from voice_generator import generate_voice
from visuals_fetcher import fetch_images
from video_builder import build_video
from subtitle_generator import generate_srt
import os

def run_pipeline(topic):
    if not os.path.exists("output"):
        os.makedirs("output")

    print("Generating script...")
    script = generate_script(topic)

    print("Generating voice...")
    generate_voice(script)

    print("Fetching visuals...")
    images = fetch_images(topic)

    print("Generating subtitles...")
    generate_srt(script)

    print("Building video...")
    build_video(images)

    print("✅ Video Ready! Check output folder.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        topic = sys.argv[1]
    else:
        topic = input("Enter Topic: ")
    run_pipeline(topic)
