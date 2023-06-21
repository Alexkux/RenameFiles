import os
my_directory = r"E:\TEMP"

def rename_files_and_dirs(path, substring):
    for filename in os.listdir(path):
        full_path = os.path.join(path, filename)
        new_filename = filename.replace(substring, "").strip()
        new_full_path = os.path.join(path, new_filename)
        os.rename(full_path, new_full_path)

        if os.path.isdir(new_full_path):
            rename_files_and_dirs(new_full_path, substring)


# Example usage: remove substring "old_" from all and directories in "my_directory"
rename_files_and_dirs("my_directory", "old_")