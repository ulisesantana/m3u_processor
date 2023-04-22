import os
import sys
from m3u_processor import read_m3u_file, get_audio_files_in_directory

YELLOW = "\033[33m"
RESET = "\033[0m"

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <m3u_file_path>")
        sys.exit(1)

    m3u_file_path = sys.argv[1]
    base_path = os.path.dirname(os.path.abspath(m3u_file_path))

    m3u_files = read_m3u_file(m3u_file_path)
    files_in_directory = get_audio_files_in_directory(base_path)

    missing_files = m3u_files - files_in_directory
    print(f"Files in M3U but not in the directory ({len(missing_files)}):")
    for file in missing_files:
        print(f"{YELLOW}{file}{RESET}")  # Yellow text

    extra_files = files_in_directory - m3u_files
    print(f"\nFiles in the directory but not in the M3U ({len(extra_files)}):")
    for file in extra_files:
        print(f"{YELLOW}{file}{RESET}")  # Yellow text

if __name__ == "__main__":
    main()
