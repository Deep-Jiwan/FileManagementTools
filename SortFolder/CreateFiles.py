import os
import random
import string


# Dictionary containing various file extensions
file_extensions = {
    "unsorted": ['csv', 'pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'ics', 'py', 'c', 'cpp', 'html', 'css', 'js', 'aep', 'prproj', 'ai', 'psd', 'jpeg', 'jpg', 'png', 'gif', 'm4a', 'mp3', 'wav', 'mp4', 'mov', 'avi', 'mkv', 'mp4', 'mov', 'avi', 'mkv', 'm4a', 'mp3', 'wav', 'msi', 'exe', 'apk', 'crdownload', 'msi', 'exe', 'exe', 'crdownload', 'apk', 'ttf', 'otf']
}

# Path of the folder where the dummy files will be created
folder_path = os.path.dirname(os.path.abspath(__file__))

# Loop through each category of file extensions
for category, extensions in file_extensions.items():
    # Loop through each extension in the category
    for ext in extensions:
        # Create 5 copies of the file with the extension
        for i in range(5):
            # Generate a random name for the file
            file_name = ''.join(random.choices(string.ascii_lowercase, k=10)) + '.' + ext
            # Create the file in the specified folder
            file_path = os.path.join(folder_path, category, file_name)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            # Generate a random size for the file between 1 MB to 20 MB
            file_size = random.randint(1, 20) * 1024 * 1024
            # Create the file with random data of the specified size
            with open(file_path, 'wb') as f:
                f.write(os.urandom(file_size))
