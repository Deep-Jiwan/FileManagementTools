import os
from faker import Faker
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas

# Set up Faker for generating sample data
fake = Faker()

# Get the current directory where the script file is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create five folders
for i in range(1, 6):
    folder_name = f"Folder_{i}"
    folder_path = os.path.join(script_dir, folder_name)
    os.makedirs(folder_path)

    # Create two JPEG files
    for j in range(1, 3):
        image_name = f"Image{j}.jpeg"
        image_path = os.path.join(folder_path, image_name)
        image = Image.new("RGB", (800, 600), "white")

        # Add sample data as text to the image
        image_text = fake.text(max_nb_chars=100)
        image_draw = ImageDraw.Draw(image)
        image_font = ImageFont.truetype("arial.ttf", 20)
        image_draw.text((50, 50), image_text, fill=(0, 0, 0), font=image_font)

        image.save(image_path)

    # Create two PDF files
    for k in range(1, 3):
        pdf_name = f"Document{k}.pdf"
        pdf_path = os.path.join(folder_path, pdf_name)
        pdf = canvas.Canvas(pdf_path)
        pdf.setTitle(pdf_name)

        # Generate sample data for the PDF
        pdf_data = fake.text(max_nb_chars=100)

        # Write the data to the PDF
        pdf.setFont("Helvetica", 12)
        pdf.drawString(100, 700, pdf_data)
        pdf.save()

    # Create a text file
    text_name = f"TextFile.txt"
    text_path = os.path.join(folder_path, text_name)
    with open(text_path, "w") as file:
        # Generate sample data for the text file
        text_data = fake.text(max_nb_chars=200)
        file.write(text_data)

print("Folders and files created successfully.")
