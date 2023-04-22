import os

def read_m3u_file(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    return set(line.strip() for line in lines if line.strip())

def get_audio_files_in_directory(base_path):
    audio_extensions = {".mp3", ".wav", ".flac"}
    files_in_directory = set()
    
    for root, dirs, files in os.walk(base_path):
        for f in files:
            if os.path.splitext(f)[1] in audio_extensions:
                files_in_directory.add(os.path.relpath(os.path.join(root, f), base_path))

    return files_in_directory
