from PyPDF2 import PdfReader, PdfWriter
import getpass

def protect_pdf(input_pdf, output_pdf):
    with open(input_pdf, 'rb') as file:
        reader = PdfReader(file)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        password = getpass.getpass("Enter a password: ")
        writer.encrypt(password)

        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)

    print("The PDF has a password.")

protect_pdf("praise.pdf", "protect_file.pdf")
