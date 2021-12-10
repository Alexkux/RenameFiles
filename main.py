import os


DIRECTORY = r"C:\TMP"

def rename_files(find_directory):
    for root, dirs, files in os.walk(find_directory):
#        for name in dirs:
#            rename_file(root, name)
        for name in files:
            rename_file(root, name)



def rename_file(root, name):
    valid_name = get_valid_name(name)
    # old_file = os.path.join(root, name) # Переименование директорий
    new_file = os.path.join(root, valid_name) # Переименование файлов
    os.rename(old_file, new_file)


def get_valid_name(name):
    name = name.replace("Иванов", "")
#    if not name.startswith("a_"):
#        name = "a_" + name
    return name


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rename_files(DIRECTORY)


