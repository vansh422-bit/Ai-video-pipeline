from moviepy.editor import *
import requests
import os

def build_video(image_urls, audio_path="output/audio.mp3"):
    print("Starting video build...")
    clips = []

    for i, url in enumerate(image_urls):
        print(f"Downloading image {i}...")
        img_data = requests.get(url).content
        img_path = f"output/img{i}.jpg"

        with open(img_path, "wb") as f:
            f.write(img_data)

        clip = ImageClip(img_path).set_duration(4)
        clips.append(clip)

    print("Concatenating clips...")
    video = concatenate_videoclips(clips, method="compose")
    print("Loading audio...")
    audio = AudioFileClip(audio_path)

    print("Setting audio to video...")
    final_video = video.set_audio(audio)
    print("Writing video file...")
    final_video.write_videofile("output/final_video.mp4", fps=24)
    print("Video built successfully!")
