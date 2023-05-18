# General instructions: 

This script uses 2 python modules that you may need to install if you plan to develop this script

    pip install pillow


    pip install pypdf2

I have made a exe, but that should only work in windows. 
The python sript does work in Mac machine but i have no idea how to make the executable.

I believe linux should also work. If anyone could test that for me and report back that it works as intended.
(You can use the CreateTest.py for this)

You can use the CreateTest.py / .exe to test out this script

I understand that making an exe might not be optimal. But in future version the exe will have a gui that the user can interact and give the script options on how to run (I dont know how to do this yet)



# What is this script?

- If you have a folder that contains different file types that you need to convert and combine into a pdf, then this is the guy!.
This sript will combine images, docs, pdf into a single pdf and rename the pdf to the name of the folder.

It will also add a number sequence at the start (01 02 03 04 05)..

# How to use.

- 1. Place the script / executable in the root of the folders that have the files to be combined.
        Meaning something like this:

            - Root Folder / CombineThis / yourfileshere.pdf

            Place the script / executable in the path 
            - Root Folder /

- 2. Cross check that all files are present and folders have the correct names (You dont need to give sequence to the folders. They will be selected alphabetically.) Your output file will take the name of the folder.
    In this case:
            - Root Folder / 00 FINAL / 01 CombineThis.pdf 

- 3. Run the script / executable and you're done!

- 4. The files will be available in the folder named "00 FINAL" - this will be editable in the future.

- 5. Make sure to check the log file for skipped files / errors. This file will be needed for debugging purposes as well.





# Script Behaviour: 

- It will combine all folders where it is run. So arrange accordingly.
- The files are combined in alphabetical ( numerical ) order.
- Log files are generated. You can use this to check if any files have been skipped or not. You should see the log file where the sript is run.
- All the final PDF will be put in a folder called 00 FINAL. (For now..)


# Features that i want to add:


- GUI customization:
    - File naming sequence
    - File exclusion
- Features:
    - Support for .heif / .heic
    - Support for other doc formats, excel formats and more...
    - Password encyption 
    - PDF compression ratio
    - (What others suggest)




Channel log:

# V1 - 18/05/2023 - First Release:
- First Release.

# V2 - dd/mm/yyyy - Second Release/ Optional Release / Mac Release
