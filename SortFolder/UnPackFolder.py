import os
import shutil

cwd = os.path.dirname(os.path.abspath(__file__))
unpack_folder = os.path.join(cwd, "unsorted")

def unpack_folder_contents(folder_path):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isdir(file_path):
            if unpack_all_folders:
                unpack_folder_contents(file_path)
                shutil.rmtree(file_path)
            else:
                while True:
                    unpack = input(f"Do you want to unpack contents of {file_path}? (y/n): ")
                    if unpack.lower() == "y":
                        unpack_folder_contents(file_path)
                        shutil.rmtree(file_path)
                        break
                    elif unpack.lower() == "n":
                        break
        else:
            new_path = os.path.join(unpack_folder, file)
            if os.path.exists(new_path):
                print(f"Skipping {file} as it already exists in {unpack_folder}")
            else:
                shutil.move(file_path, new_path)

if not os.path.exists(unpack_folder):
    os.mkdir(unpack_folder)

unpack_all_folders = input("Do you want to unpack all folders? (y/n): ").lower() == "y"

for folder in os.listdir(cwd):
    folder_path = os.path.join(cwd, folder)
    if os.path.isdir(folder_path) and folder != "unsorted":
        if not unpack_all_folders:
            unpack_folder_contents(folder_path)
            os.rmdir(folder_path)
        else:
            unpack_folder_contents(folder_path)
            shutil.rmtree(folder_path)
