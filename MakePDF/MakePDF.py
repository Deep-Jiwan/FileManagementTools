import os
import sys
from PIL import Image
from PyPDF2 import PdfWriter, PdfReader
import datetime

# Get the directory path of the script
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(script_dir)


# Function to convert image files to PDF
def convert_image_to_pdf(image_path, pdf_writer):
    image = Image.open(image_path)
    pdf_path = image_path[:-4] + ".pdf"  # Create a PDF file path by replacing the image file extension
    image.save(pdf_path, "PDF", resolution=100.0)
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        pdf_writer.add_page(pdf_reader.pages[0])
    os.remove(pdf_path)  # Remove the temporary PDF file

log_file_path = os.path.join(script_dir, "log.txt")


# Function to combine files from a folder into a single PDF document
def combine_files(main_folder, output_folder):
    folder_counter = 1
    folders = sorted(os.listdir(main_folder))  # Sort the folders alphabetically

    for folder_name in folders:
        folder_path = os.path.join(main_folder, folder_name)
        if os.path.isdir(folder_path) and folder_name != "00 FINAL" and folder_name != "_pycache_":  # Skip the "FINAL" folder
            pdf_writer = PdfWriter()
            for root, _, files in os.walk(folder_path):
                for filename in sorted(files):  # Sort files alphabetically
                    file_path = os.path.join(root, filename)
                    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
                        convert_image_to_pdf(file_path, pdf_writer)
                    elif filename.lower().endswith(".pdf"):
                        with open(file_path, "rb") as pdf_file:
                            pdf_reader = PdfReader(pdf_file)
                            for page in pdf_reader.pages:
                                pdf_writer.add_page(page)
                    else:
                        print(f"\nSkipping file '{file_path}' due to unsupported extension.")
                        log_message = f"\nSkipping file '{file_path}' due to unsupported extension."
                        with open(log_file_path, "a") as log_file:
                            log_file.write(log_message)

            output_pdf_path = os.path.join(output_folder, f"{folder_counter:02d} {folder_name}.pdf")  # Rename file with number and folder name
            with open(output_pdf_path, "wb") as output_pdf:
                pdf_writer.write(output_pdf)

            log_message = f"\nCombined files from folder '{folder_path}' into PDF: {output_pdf_path}"
            print(log_message)
            with open(log_file_path, "a") as log_file:
                log_file.write(log_message)

            folder_counter += 1

# Set the main folder to be the script directory
main_folder = script_dir

# Check if the main folder exists
if os.path.isdir(main_folder):
    # Create the FINAL folder if it doesn't exist
    output_folder = os.path.join(main_folder, "00 FINAL")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    start_time = datetime.datetime.now()

    combine_files(main_folder, output_folder)

    end_time = datetime.datetime.now()
    duration = end_time - start_time

    print(f"\n\nAll files combined into PDF documents in the '00 FINAL' folder.")
    print(f"Process duration: {duration}")

    with open(log_file_path, "a") as log_file:
        log_file.write(f"\nAll files combined into PDF documents in the '00 FINAL' folder.")
        log_file.write(f"\nProcess duration: {duration}")
else:
    print("\n\nMain folder does not exist.")

