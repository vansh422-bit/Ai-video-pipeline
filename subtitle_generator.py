def generate_srt(script):
    lines = script.split(".")
    with open("output/subtitles.srt", "w", encoding="utf-8") as f:
        for i, line in enumerate(lines):
            f.write(f"{i+1}\n")
            f.write(f"00:00:{i*4:02d},000 --> 00:00:{(i+1)*4:02d},000\n")
            f.write(line.strip() + "\n\n")
