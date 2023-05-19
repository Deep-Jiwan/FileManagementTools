import os
import sys
import random
import string
import time

# Dictionary containing various file extensions
file_extensions = {
    "unsorted": ['csv', 'pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'ics', 'py', 'c', 'cpp', 'html', 'css', 'js', 'aep', 'prproj', 'ai', 'psd', 'jpeg', 'jpg', 'png', 'gif', 'm4a', 'mp3', 'wav', 'mp4', 'mov', 'avi', 'mkv', 'mp4', 'mov', 'avi', 'mkv', 'm4a', 'mp3', 'wav', 'msi', 'exe', 'apk', 'crdownload', 'msi', 'exe', 'exe', 'crdownload', 'apk', 'ttf', 'otf']
}

# Path of the folder where the dummy files will be created
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(script_dir)

# Function to display progress bar
def print_progress_bar(iteration, total, prefix='', suffix='', length=30, fill='█'):
    percent = '{0:.1f}'.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if iteration == total:
        print()

# Calculate the total number of files to create
total_files = sum(len(extensions) for extensions in file_extensions.values()) * 5
print(f"Creating {total_files} files now.")

# Initialize counters
progress = 0
current_file = 0

# Loop through each category of file extensions
for category, extensions in file_extensions.items():
    # Loop through each extension in the category
    for ext in extensions:
        # Create 5 copies of the file with the extension
        for i in range(5):
            # Generate a random name for the file
            file_name = ''.join(random.choices(string.ascii_lowercase, k=10)) + '.' + ext
            # Create the file in the specified folder
            file_path = os.path.join(script_dir, category, file_name)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            # Generate a random size for the file between 1 MB to 20 MB
            file_size = random.randint(1, 20) * 1024 * 1024
            # Create the file with random data of the specified size
            with open(file_path, 'wb') as f:
                f.write(os.urandom(file_size))
            # Update progress counters
            current_file += 1
            progress_percentage = current_file / total_files * 100
            # Update progress bar
            print_progress_bar(progress_percentage, 100, prefix='Progress:', suffix='Complete', length=30)
            #time.sleep(0.1)  # Add a slight delay for better visualization

print("All files created successfully!")

time.sleep(5)