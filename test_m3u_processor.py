import unittest
import os
from m3u_processor import read_m3u_file, get_audio_files_in_directory


class TestM3UProcessor(unittest.TestCase):
    def test_read_m3u_file_duplicates_invalid(self):
        with open("test_duplicates_invalid.m3u", "w") as f:
            f.write("test1.mp3\ntest1.mp3\ninvalid_path.mp3\n")

        m3u_files = read_m3u_file("test_duplicates_invalid.m3u")
        self.assertEqual(m3u_files, {"test1.mp3", "invalid_path.mp3"})

    def test_get_audio_files_nested_directories(self):
        os.makedirs("test_nested_dir/level1/level2", exist_ok=True)
        with open("test_nested_dir/test1.mp3", "w") as f1, open(
            "test_nested_dir/level1/test2.flac", "w"
        ) as f2, open("test_nested_dir/level1/level2/test3.wav", "w") as f3:
            pass

        files_in_directory = get_audio_files_in_directory("test_nested_dir")
        self.assertEqual(
            files_in_directory,
            {
                "test1.mp3",
                os.path.join("level1", "test2.flac"),
                os.path.join("level1", "level2", "test3.wav"),
            },
        )

        # Clean up test files and directories
        os.remove("test_nested_dir/test1.mp3")
        os.remove("test_nested_dir/level1/test2.flac")
        os.remove("test_nested_dir/level1/level2/test3.wav")
        os.rmdir("test_nested_dir/level1/level2")
        os.rmdir("test_nested_dir/level1")
        os.rmdir("test_nested_dir")

    def test_get_audio_files_special_chars(self):
        os.makedirs("test_special_chars", exist_ok=True)
        with open("test_special_chars/áéíóú.mp3", "w") as f1, open(
            "test_special_chars/!@#$%^&*().wav", "w"
        ) as f2, open("test_special_chars/with space.flac", "w") as f3:
            pass

        files_in_directory = get_audio_files_in_directory("test_special_chars")
        self.assertEqual(
            files_in_directory, {"áéíóú.mp3", "!@#$%^&*().wav", "with space.flac"}
        )

        # Clean up test files and directories
        os.remove("test_special_chars/áéíóú.mp3")
        os.remove("test_special_chars/!@#$%^&*().wav")
        os.remove("test_special_chars/with space.flac")
        os.rmdir("test_special_chars")

    def test_get_audio_files_m3u_empty(self):
        with open("test_empty.m3u", "w") as f:
            pass

        m3u_files = read_m3u_file("test_empty.m3u")
        self.assertEqual(m3u_files, set())

    def test_get_audio_files_empty_directory(self):
        os.makedirs("test_empty_dir", exist_ok=True)

        files_in_directory = get_audio_files_in_directory("test_empty_dir")
        self.assertEqual(files_in_directory, set())

        # Clean up test directory
        os.rmdir("test_empty_dir")

    def test_read_m3u_file_falsy_lines(self):
        with open("test_falsy_lines.m3u", "w") as f:
            f.write("test1.mp3\n\n  \n\t\ninvalid_path.mp3\n")

        m3u_files = read_m3u_file("test_falsy_lines.m3u")
        self.assertEqual(m3u_files, {"test1.mp3", "invalid_path.mp3"})


if __name__ == "__main__":
    unittest.main()
