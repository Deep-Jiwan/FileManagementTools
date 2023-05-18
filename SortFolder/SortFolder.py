import os
import shutil
import time

cwd = "C:/Users/Deep/Downloads/"
unsorted_folder_path = cwd#os.path.join(cwd, "unsorted")

# create the folders if they don't exist
folders = {
    "Documents/MS Word": ["doc", "docx"],
    "Documents/MS Excel": ["xls", "xlsx", "csv"],
    "Documents/MS Powerpoint": ["ppt", "pptx"],
    "Documents/PDFs": ["pdf"],
    "Documents/Calender": ["ics"],
    "Programming and Development/C and C++": ["c", "cpp"],
    "Programming and Development/Python": ["py"],
    "Programming and Development/HTML, JS and CSS": ["html", "css", "js"],
    "Creative/After Effects": ["aep"],
    "Creative/Premier Pro": ["prproj"],
    "Creative/Photoshop and Illustrator": ["ai", "psd"],
    "Creative/Images": ["jpeg", "jpg", "png", "gif"],
    "Multimedia/Video": ["mp4", "mov", "avi", "mkv"],
    "Multimedia/Audio": ["m4a", "mp3", "wav"],
    "Softwares/MSI": ["msi"],
    "Softwares/EXE Big": ["exe"],
    "Softwares/EXE Small": ["exe"],
    "Softwares/Cr Downloads": ["crdownload"],
    "Softwares/Android APKs": ["apk"],
    "Fonts": ["ttf", "otf"]
}



# convert all extensions to lowercase
for folder_name, extensions in folders.items():
    folders[folder_name] = [extension.lower() for extension in extensions]

# start the timer
start_time = time.time()

for folder_name, extensions in folders.items():
    folder_path = os.path.join(cwd, folder_name)
    os.makedirs(folder_path, exist_ok=True)

for item_name in os.listdir(unsorted_folder_path):
    item_path = os.path.join(unsorted_folder_path, item_name)
    if os.path.isfile(item_path):
        try:
            extension = item_name.split(".")[-1].lower()
            for folder_name, extensions in folders.items():
                if extension in extensions:
                    if "/" in folder_name:
                        subfolder_name = folder_name.split("/")[-1]
                        folder_name = "/".join(folder_name.split("/")[:-1])
                        subfolder_path = os.path.join(cwd, folder_name, subfolder_name)
                        os.makedirs(subfolder_path, exist_ok=True)
                        new_path = os.path.join(subfolder_path, item_name)
                    else:
                        new_path = os.path.join(cwd, folder_name, item_name)
                    shutil.move(item_path, new_path)
                    print(f"Moved {item_name} to {new_path}.")
                    break
            else:
                print(f"Could not sort {item_name}.")
        except Exception as e:
            print(f"Error occurred while sorting {item_name}: {e}")
    elif os.path.isdir(item_path):
        print(f"Skipping {item_name} as it is a directory.")

# end the timer
end_time = time.time()

# calculate the time taken
time_taken = end_time - start_time

# print the result
print(f"Time taken to sort: {time_taken} seconds")